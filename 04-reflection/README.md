# Chapter 4: Reflection

The Reflection pattern involves an agent evaluating its own work, output, or internal state and using the evaluation to improve its performance or refine its response. It's a form of self-correction or self-improvement, allowing the agent to iteratively refine its output or adjust its approach based on feedback, internal critique, or comparison against desired criteria.


## Features
- The implementation of a complete, iterative reflection process necessitates mechanisms for state management and cyclical execution. 
- The example in code implements a reflection loop using the LangChain library to iteratively generate and refine a Python function that calculates the factorial of a number.
- The process starts with a task prompt, generates initial code, and then repeatedly reflects on the code based on critiques from a simulated senior software engineer role, refining the code in each iteration until the critique stage determines the code is perfect.


## How to Get Started
1. Clone the repository:
```bash
git clone https://github.com/wenyuliuinfo/agentic-design-learning-path.git
cd 04-reflection/python
```

2. Install the prerequisites:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U -r requirements.txt
```

3. Run the application:
```bash
python reflection.py
```