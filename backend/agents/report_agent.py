from backend.llm import llm

from backend.utils.report_manager import (
    save_report
)


def generate_report(state):

    query = state.get(
        "query",
        ""
    )

    analysis = state.get(
        "analysis",
        ""
    )

    source_documents = state.get(
        "source_documents",
        []
    )

    sources = []

    for doc in source_documents:

        sources.append(

            f"""
Company:
{doc.get('company')}

Source:
{doc.get('source')}
"""
        )

    sources_text = "\n".join(
        sources
    )

    prompt = f"""
You are a senior financial analyst.

Research Topic:
{query}

Analysis:
{analysis}

Sources:
{sources_text}

Generate a professional report.

Structure:

# Executive Summary

# Market Overview

# Competitive Landscape

# Financial Analysis

# Annual Report Insights

# Opportunities

# Risks

# Future Outlook

# Investment View

Bull Case

Base Case

Bear Case

# Conclusion

# Sources Used

Keep report concise and factual.
"""

    response = llm.invoke(
        prompt
    )

    report = response.content

    filepath = save_report(
        report
    )

    print("=" * 50)
    print("PDF SAVED")
    print(filepath)
    print("=" * 50)

    state["final_report"] = report

    state["report_path"] = filepath

    return state