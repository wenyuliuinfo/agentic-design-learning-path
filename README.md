# Agentic Design Learning Path

This repository is a practical, code-first exploration of the foundational patterns and architectures for building robust, intelligent AI agents. It is based on the book *"Agentic Design Patterns"* and provides hands-on Python implementations of key agentic concepts.

## 🎯 About This Repository

The goal of this learning path is to move beyond simple LLM calls and equip you with the skills to design and build complex, autonomous AI systems. You will learn by implementing the core patterns that make agents effective: how they reason, plan, use tools, manage memory, and interact with their environment.

This is not a theoretical course. Each module provides executable code that demonstrates a specific agentic design pattern, allowing you to experiment, modify, and internalize these powerful concepts.

## 📂 Repository Structure

The content is organized into modules, each focusing on a specific agentic design pattern.

```
agentic-design-learning-path/
├── 01-prompt-chaining/             # Breaking down tasks into sequential prompts
├── 02-routing/                     # Directing tasks to specialized sub-agents
├── 03-parallelization/             # Running multiple agent processes concurrently
├── 04-reflection/                  # Agents critiquing and improving their own outputs
├── 05-tool-use/                    # Enabling agents to interact with external tools
├── 08-memory-management/           # Managing short-term and long-term agent memory
├── 11-goal-setting/                # Agents setting and monitoring their own goals
├── 14-knowledge-retrieval/         # Integrating RAG and knowledge bases
├── 16-resource-aware-optimization/ # Optimizing agent performance with resource constraints
├── 18-guardrails-patterns/         # Implementing safety and control mechanisms
├── 19-evaluation-and-monitoring/   # Measuring and tracking agent performance
├── 20-prioritization/              # Managing and prioritizing multiple tasks/goals
├── .env.example                    # Example environment variables file
├── .gitignore
└── README.md
```

Each module folder typically contains:
- **`README.md`**: A detailed explanation of the pattern, its use cases, and how the code works.
- **`.py` Python scripts**: The core implementation of the pattern.
  

## 🚀 Getting Started

### Prerequisites

To effectively use this repository, you should have:
- Solid knowledge of Python programming.
- A basic understanding of LLMs and the LangChain framework.
- An API key for an LLM provider (e.g., OpenAI, Azure OpenAI, Anthropic).

### Installation & Running the Code

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/wenyuliuinfo/agentic-design-learning-path.git
    cd agentic-design-learning-path
    ```

2. **Set up a Python environment:**
It's highly recommended to use a virtual environment.
    ```bash
    # Using venv (Python 3.9+)
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
(Note: A `requirements.txt` may not be present in the root. Check each module folder or install core libraries like `langchain`, `openai`, and `python-dotenv` globally.)

4. **Set up your API Keys:**
Most modules will require an API key. Copy the .env.example file to .env in the root directory and add your keys:
    ```bash
    cp .env.example .env
    # Edit .env with your credentials (e.g., OPENAI_API_KEY="your-key-here")
    ```

5. **Run a Module:**
Navigate into a module folder and execute the main Python script.
    ```bash
    cd 01-prompt-chaining/python
    python prompt_chaining.py  # Example command
    ```

## 🧠 Key Topics & Learning Path
This repository is structured to guide you through the most important agentic design patterns. The modules are organized roughly by complexity, though you can explore them in any order.

#### 1. Foundational Reasoning Patterns
- **Prompt Chaining** (`01-prompt-chaining`): Learn to break complex tasks into a sequence of simpler, focused prompts. This is the foundation for reliable, step-by-step agent reasoning.
- **Routing** (`02-routing`): Implement logic to classify inputs and route them to the most appropriate specialized sub-agent or prompt template.
- **Parallelization** (`03-parallelization`): Explore patterns where multiple agents or tasks are executed concurrently to improve efficiency.

#### 2. Core Agentic Capabilities
- **Reflection** (`04-reflection`): Build agents that can critique and improve their own outputs, leading to higher quality and more reliable results.
- **Tool Use** (`05-tool-use`): Enable your agents to interact with the outside world by defining and calling functions (APIs, web search, databases, etc.).
- **Memory Management** (`08-memory-management`): Implement different memory strategies (short-term, long-term, summary) to give your agents context and continuity.

#### 3. Advanced System Design
- **Goal Setting & Monitoring** (`11-goal-setting`): Design agents that can plan and monitor their progress toward achieving complex, self-directed objectives.
- **Knowledge Retrieval** (`14-knowledge-retrieval`): Integrate Retrieval-Augmented Generation (RAG) to ground agents in proprietary or up-to-date information.
- **Resource-Aware Optimization** (`16-resource-aware-optimization`): Learn to manage and optimize agent performance under constraints like cost, latency, and token usage.

#### 4. Production-Ready Patterns
- **Guardrails** (`18-guardrails-patterns`): Implement safety mechanisms, input/output validation, and content moderation to ensure your agents behave as expected.
- **Evaluation & Monitoring** (`19-evaluation-and-monitoring`): Set up frameworks to measure agent performance and system health in production.
- **Prioritization** (`20-prioritization`): Manage multiple tasks, goals, and agents by implementing effective prioritization strategies.
