from typing import TypedDict


class ResearchState(TypedDict):

    query: str

    sector: str

    approved: bool

    research_plan: str

    current_query: str

    search_history: list

    findings: list

    reasoning_chain: list

    financial_metrics: dict

    rag_context: str

    source_documents: list

    analysis: str

    final_report: str

    report_path: str