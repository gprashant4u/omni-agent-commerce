# OmniAgent Commerce Engine

An advanced multi-agent orchestration platform designed for autonomous commerce operations.

## 🚀 Key Features vs. Requirements
- **Agentic Frameworks**: Built using **LangChain** and **CrewAI** for multi-agent collaboration .
- **Orchestration Patterns**: Implements a **Planner/Executor** pattern with specialized agents for Concierge and Inventory tasks .
- **RAG & Vector DB**: Grounded search using **FAISS** for semantic product retrieval .
- **Architecture**: **MCP (Model Context Protocol)**-inspired plugin system for commerce platform extensibility .
- **Backend**: **FastAPI** microservice architecture with **Python** .
- **Observability**: Custom decorators for **latency profiling** and system performance monitoring .

## 🛠️ Project Structure
- pi.py: FastAPI entry point for microservice interaction.
- main.py: Core Agentic orchestration and task definitions.
- gents/: Specialized agent logic (Concierge/Inventory).
- 	ools/: RAG and Vector DB tools.
- plugins/: MCP-compliant integration layer.
- utils.py: Observability and performance profiling.

## ⚙️ Setup
1. Install dependencies: pip install -r requirements.txt
2. Run the API: python api.py
