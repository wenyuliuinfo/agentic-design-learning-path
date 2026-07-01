# Chapter 11: Goal Setting and Monitoring

For AI Agents to be truly effective and purposeful, they need more than just the ability to process information or use tools; they need a clear sense of direction and a way to know if they're actually succeeding. This is where the Goal Setting and Monitoring pattern comes into play. It's about giving agents specific objectives to work towards and equipping them with the means to track their progress and determine if those objectives have been met.


## Features
- To illustrate the Goal Setting and Monitoring pattern, we have an example using LangChain. This Python script outlines an autonomous AI agent engineered to generate and refine Python code. Its core function is to produce solutions for specified problems, ensuring adherence to user-defined quality benchmarks.
- It employs a "goal-setting and monitoring" pattern where it doesn't just generate code once, but enters into an iterative cycle of creation, self-evaluation, and improvement.
- The agent's success if measured by its own AI-driven judgement on whether the generated code successfully meets the initial objectives. The ultimate output is a polished, commented, and ready-to-use Python file that represents the culmination of this refinement process.


## How to Get Started
1. Clone the repository:
```bash
git clone https://github.com/wenyuliuinfo/agentic-design-learning-path.git
cd 11-goal-setting/python
```

2. Install the prerequisites:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U -r requirements.txt
```

3. Run the application:
```bash
python goal_setting.py
```