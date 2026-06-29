import os
from typing import List
from dotenv import load_dotenv
from operator import itemgetter

from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_community.chat_message_histories import ChatMessageHistory

# --- Configuration ---
load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")

llm = ChatOpenAI(
    model="deepseek-v4-pro",  # Or "deepseek-v4-flash" for a faster option
    openai_api_key=DEEPSEEK_API_KEY,
    openai_api_base=DEEPSEEK_BASE_URL, 
    temperature=0
)

# --- For Manual Memory Management ---
history = ChatMessageHistory()

history.add_user_message("I'm heading to Shanghai next week.")
history.add_ai_message("Great! It's a fantastic city.")
print(history.messages)

# --- For Automated Memory for Chains ---
# 1. Define the LLM and Prompt
template = """
    You are a helpful travel agent.
    Previous conversation: {history}
    New question: {question}
    Response:
"""
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful travel agent."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}"),
])

# 2. Configure Memory
memory = ConversationBufferMemory(memory_key="history", return_messages=True)

# 3. Build the Chain
#conversation = LLMChain(llm=llm, prompt=prompt, memory=memory)
conversation = RunnablePassthrough.assign(history=RunnableLambda(lambda x: memory.load_memory_variables(x)["history"])) | prompt | llm | StrOutputParser()

# 4. Run the Conversation
response = conversation.invoke({"question": "I want to book a flight."})
memory.save_context({"input": "I want to book a flight."}, {"output": response})
print(response)
response = conversation.invoke({"question": "My name is Sam."})
memory.save_context({"input": "My name is Sam."}, {"output": response})
print(response)
response = conversation.invoke({"question": "What was my name again?"})
memory.save_context({"input": "What was my name again?"}, {"output": response})
print(response)

