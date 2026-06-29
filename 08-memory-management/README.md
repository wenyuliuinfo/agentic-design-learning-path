# Chapter 8: Memory Management

In agent systems, memory refers to an agent's ability to retain and utilize information from past interactions, observations, and learning experiences. This capability allows agents to make informed decisions, maintain conversational context, and improve over time.


## Features
- In LangChain and LangGraph, Memory allows an AI agent to remember information from past interactions, learn from feedback, and adapt to user preferences.
- Short-Term Memory: This is thread-scoped, meaning it tracks the ongoing conversation within a single session or thread. It provides immediate context, but a full history can challenge an LLM's context window, potentially leading to errors or poor performance. LangGraph manages short-term memory as part of the agent's state, which is persisted via a checkpointer, allowing a thread to be resumed at any time.
- Long-Term Memory: This stores user-specific or application-level data across sessions and is shared between conversational threads. It is saved in custom namespaces and can be recalled at any time in any thread. LangGraph provides stores to save and recall long-term memories, enabling agents to retain knowledge indefinitely.


## How to Get Started
1. Clone the repository:
```bash
git clone https://github.com/wenyuliuinfo/agentic-design-learning-path.git
cd 08-memory-management/python
```

2. Install the prerequisites:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U -r requirements.txt
```

3. Run the application:
```bash
python memory.py
```