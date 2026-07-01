# Financial Research Agent Architecture

User
 │
 ▼
Streamlit UI
 │
 ▼
LangGraph Workflow
 │
 ├── Router Agent
 │
 ├── Planner Agent
 │
 ├── Research Agent
 │      │
 │      └── Tavily Search
 │
 ├── Financial Agent
 │      │
 │      └── Yahoo Finance
 │
 ├── RAG Agent
 │      │
 │      └── Pinecone
 │
 ├── Analyzer Agent
 │
 └── Report Agent
 │
 ▼
Research Report