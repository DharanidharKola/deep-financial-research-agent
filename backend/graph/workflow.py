from backend.agents.rag_agent import (retrieve_context)

from langgraph.graph import StateGraph, END

from backend.models.state import ResearchState

# Agents
from backend.agents.router_agent import route_query
from backend.agents.planner_agent import create_plan
from backend.agents.researcher_agent import research_loop
from backend.agents.financial_agent import collect_financials
from backend.agents.analyzer_agent import analyze_findings
from backend.agents.report_agent import generate_report


# Create Graph
builder = StateGraph(ResearchState)

# -----------------------------
# Nodes
# -----------------------------

builder.add_node(
    "router",
    route_query
)

builder.add_node(
    "planner",
    create_plan
)

builder.add_node(
    "research",
    research_loop
)

builder.add_node(
    "financial",
    collect_financials
)

builder.add_node(
    "rag",
    retrieve_context
)

builder.add_node(
    "analyzer",
    analyze_findings
)

builder.add_node(
    "report",
    generate_report
)

# -----------------------------
# Flow
# -----------------------------

builder.set_entry_point(
    "router"
)

builder.add_edge(
    "router",
    "planner"
)

builder.add_edge(
    "planner",
    "research"
)

builder.add_edge(
    "research",
    "financial"
)

builder.add_edge(
    "financial",
    "rag"
)

builder.add_edge(
    "rag",
    "analyzer"
)

builder.add_edge(
    "analyzer",
    "report"
)

builder.add_edge(
    "report",
    END
)

# -----------------------------
# Compile
# -----------------------------

graph = builder.compile()