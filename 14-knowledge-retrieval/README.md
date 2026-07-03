# Chapter 14: Knowledge Retrieval (RAG)

Knowledge Retrieval (RAG, or Retrieval Augmented Generation) enables LLMs to access and integrate external, current, and context-specific information, thereby enhancing the accuracy, relevance, and factual basis of their outputs.


## Features
- The process begins with the creation of a knowledge base derived from a text document, which is segmented into chunks and transformed into embeddings. These embeddings are then stored in a Weaviate vector store, facilitating efficient information retrieval.
- A StateGraph in LangGraph is utilized to manage the workflow between two key functions: `retrieve_documents_node` and `generate_response_node`. 
- The `retrieve_documents_node` function queries the vector store to identify relevant document chunks based on the user's input.
- The `generate_response_node` function utilizes the retrieved information and predefined prompt template to produce a response using an LLM.
- The `app.stream` method allows the execution of queries through the RAG pipeline, demonstrating the system's capacity to generate contextually relevant outputs.


## How to Get Started
1. Clone the repository:
```bash
git clone https://github.com/wenyuliuinfo/agentic-design-learning-path.git
```

2. Start the Weaviate with Docker
```bash
cd 14-knowledge-retrieval/infra
docker compose up -d
```

3. Install the prerequisites:
```bash
cd ../python
python3 -m venv .venv
source .venv/bin/activate
pip install -U -r requirements.txt
```

4. Run the application:
```bash
python rag.py
```