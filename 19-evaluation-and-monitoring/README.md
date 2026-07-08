# Chapter 19: Evaluation and Monitoring

This chapter examines methodologies that allow intelligent agents to systematically assess their performance, monitor progress toward goals, and detect operational anomalies. This chapter focuses on the continuous, often external, measurement of an agent's effectiveness, efficiency, and compliance with requirements.


## Features
- Evaluating subjective qualities like an AI agent's "helpfulness" presents challenges beyond standard objective metrics.
- A potential framework involves using an LLM as an evaluator. This LLM-as-a-Judge approach assesses another AI agent's output based on predefined criteria for "helpfulness".
- Leveraging the advanced linguistic capabilities of LLMs, this method offers nuanced, human-like evaluations of subjective qualities, surpassing simple keyword matching or rule-based assessments.


## How to Get Started
1. Clone the repository:
```bash
git clone https://github.com/wenyuliuinfo/agentic-design-learning-path.git
cd 19-evaluation-and-monitoring/python
```

2. Install the prerequisites:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U -r requirements.txt
```

3. Run the application:
```bash
python evaluation.py
```