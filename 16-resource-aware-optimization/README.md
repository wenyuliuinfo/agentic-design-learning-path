# Chapter 16: Resource-Aware Optimization

Resource-Aware Optimization enables intelligent agents to dynamically monitor and manage computational, temporal, and financial resources during operation. This differs from simple planning, which primarily focuses on action sequencing. 

Resource-Aware Optimization requires agents to make decisions regarding action execution to achieve goals within specified resource budgets or to optimize efficiency. This involves choosing between more accurate but expensive models and faster, lower-cost ones, or deciding whether to allocate additional compute for a more refined response versus returning a quicker, less detailed answer.


## Features
- This system uses a resource-aware optimization strategy to handle user queries efficiently. It first classifies each query into one of three categories to determine the most appropriate and cost-effective processing pathway.
- Simple: For straightforward questions that can be answered directly without complex reasoning or external data.
- Reasoning: For queries that require logical deduction or multi-step thought processes, which are routed to more powerful models.
- Internet_search: For questions needing current information, which automatically triggers a Google Search to provide an up-to-date answer.


## How to Get Started
1. Clone the repository:
```bash
git clone https://github.com/wenyuliuinfo/agentic-design-learning-path.git
cd 16-resource-aware-optimization/python
```

2. Install the prerequisites:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U -r requirements.txt
```

3. Run the application:
```bash
python resource_aware_optimization.py
```