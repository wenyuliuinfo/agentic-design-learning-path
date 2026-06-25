# Chapter 2: Routing

Routing introduces conditional logic into an agent's operational framework, enabling a shift from a fixed execution path to a model where the agent dynamically evaluates specific criteria to select from a set of possible subsequent actions. This allows for more flexible and context-aware system behavior.


## Features
- Implementing routing in code involves defining the possible paths and the logic that decides which path to take.
- Frameworks like LangChain and LangGraph provide specific components and structures for this. 
- LangGraph's state-based graph structure is particularly intuitive for visualizing and implementing routing logic.


## How to Get Started
1. Clone the repository:
```bash
git clone https://github.com/wenyuliuinfo/agentic-design-learning-path.git
cd 02-routing/python
```

2. Install the prerequisites:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U -r requirements.txt
```

3. Run the application:
```bash
python routing.py
```