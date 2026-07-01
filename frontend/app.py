import streamlit as st

st.set_page_config(
    page_title="Deep Financial Research Agent",
    page_icon="📈",
    layout="wide"
)

st.title(
    "📈 Deep Financial Research Agent"
)

st.caption(
    "Powered by LangGraph • Pinecone • Tavily • Groq"
)

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:

    st.subheader(
        "AI-Powered Financial Research System"
    )

    st.markdown(
        """
### Features

✅ Multi-Agent Workflow

✅ LangGraph Orchestration

✅ Tavily Web Search

✅ Yahoo Finance Integration

✅ Pinecone RAG

✅ Annual Report Analysis

✅ Financial Metrics Extraction

✅ Investment Research Reports

✅ Streamlit Dashboard
"""
    )

with col2:

    st.metric(
        "Agents",
        "7"
    )

    st.metric(
        "Vector Database",
        "Pinecone"
    )

    st.metric(
        "LLM",
        "Groq"
    )

st.markdown("---")

st.subheader(
    "System Architecture"
)

st.code(
"""
User Query
    │
    ▼
Router Agent
    │
    ▼
Planner Agent
    │
    ▼
Research Agent
(Tavily Search)
    │
    ▼
Financial Agent
(Yahoo Finance)
    │
    ▼
RAG Agent
(Pinecone)
    │
    ▼
Analyzer Agent
    │
    ▼
Report Agent
    │
    ▼
Investment Research Report
"""
)

st.markdown("---")

st.subheader(
    "Supported Sectors"
)

col1, col2 = st.columns(2)

with col1:

    st.success(
        "Information Technology (IT)"
    )

with col2:

    st.success(
        "Pharmaceuticals"
    )