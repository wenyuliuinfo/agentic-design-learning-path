import os
import requests
import weaviate
from typing import List, Dict, Any, TypedDict 
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.embeddings import ZhipuAIEmbeddings
from langchain_weaviate import WeaviateVectorStore 
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langgraph.graph import StateGraph, END

# --- Configuration ---
load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")
ZHIPUAI_API_KEY = os.getenv("ZHIPUAI_API_KEY")
ZHIPUAI_BASE_URL = os.getenv("ZHIPUAI_BASE_URL")

llm = ChatOpenAI(
    model="deepseek-v4-pro",  # Or "deepseek-v4-flash" for a faster option
    openai_api_key=DEEPSEEK_API_KEY,
    openai_api_base=DEEPSEEK_BASE_URL, 
    temperature=0
)

# --- 1. Data Preparation (Preprocessing) ---
url = "https://github.com/langchain-ai/langchain/blob/master/docs/docs/how_to/state_of_the_union.txt"
res = requests.get(url)

with open("state_of_the_union.txt", "w") as f:
    f.write(res.text)

loader = TextLoader('./state_of_the_union.txt')
documents = loader.load()

# Chunk documents
text_splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separator="",
    keep_separator=False,
    length_function=len,
)
chunks = text_splitter.split_documents(documents)

# Initialize the embedding
zhipu_embeddings = ZhipuAIEmbeddings(
    api_key=ZHIPUAI_API_KEY,
    api_base=ZHIPUAI_BASE_URL,
    model="embedding-3"
)

# Embed and store chunks in Weaviate
BATCH_SIZE = 64
client = weaviate.connect_to_local()

# Extract texts and metadatas manually
texts = [chunk.page_content for chunk in chunks]
metadata = [chunk.metadata for chunk in chunks]

vectorestore = WeaviateVectorStore.from_documents(
    client=client,
    documents=chunks[:BATCH_SIZE],
    embedding=zhipu_embeddings,
)

# Add remaining batches
for i in range(BATCH_SIZE, len(texts), BATCH_SIZE):
    vectorestore.add_texts(
        texts=texts[i:i+BATCH_SIZE],
        metadatas=metadata[i:i+BATCH_SIZE]
    )

# Define the retriever
retriever = vectorestore.as_retriever()

# --- 2. Define the State for LangGraph ---
class RAGGraphState(TypedDict):
    question: str
    documents: List[str]
    generation: str

# --- 3. Define the Nodes (Functions) ---
def retrieve_documents_node(state: RAGGraphState) -> RAGGraphState:
    """
    Retrieves documents based on the user's question.
    """
    question = state["question"]
    documents = retriever.invoke(question)
    return {"documents": documents, "question": question, "generation": ""}

def generate_response_node(state: RAGGraphState) -> RAGGraphState:
    """
    Generates a response using the LLM based on retrieved documents.
    """
    question = state["question"]
    documents = state["documents"]

    # Format the context form the documents
    context = "\n\n".join([doc.page_content for doc in documents])

    template = """
        You are an assistant for question-answering tasks. Use the following pieces of retrieved
        context to answer the question.
        If you don't know the answer, just say that you don't know. Use three sentences max and keep
        the answer concise.
        Question: {question}
        Context: {context}
        Answer:
    """
    prompt = ChatPromptTemplate.from_template(template)
    rag_chain = prompt | llm | StrOutputParser()

    # Invoke the chain
    generation = rag_chain.invoke({"context": context, "question": question})
    return {"documents": documents, "question": question, "generation": generation}

# --- 4. Build the LangGraph Graph ---
workflow = StateGraph(RAGGraphState)
workflow.add_node("retrieve", retrieve_documents_node)
workflow.add_node("generation", generate_response_node)

# Set the entry point
workflow.set_entry_point("retrieve")

# Add edges
workflow.add_edge("retrieve", "generation")
workflow.add_edge("generation", END)

app = workflow.compile()

# --- 5. Run the RAG ---
if __name__ == "__main__":
    print("\n--- Running RAG Query ---")
    query = "What are the information about Justice Breyer?"
    inputs = {"question": query}
    for s in app.stream(inputs):
        print(s)
    client.close()
    