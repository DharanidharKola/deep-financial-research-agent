from backend.llm import llm


def analyze_findings(state):

    findings = state.get(
        "findings",
        []
    )

    financial_metrics = state.get(
        "financial_metrics",
        {}
    )

    rag_context = state.get(
        "rag_context",
        ""
    )

    # ----------------------------------
    # Limit Research Findings
    # ----------------------------------

    findings_text = "\n\n".join(

        str(finding)[:500]

        for finding in findings[-3:]

    )

    # ----------------------------------
    # Limit RAG Context
    # ----------------------------------

    rag_text = str(
        rag_context
    )[:2500]

    # ----------------------------------
    # Financial Summary
    # ----------------------------------

    financial_summary = []

    for company, data in financial_metrics.items():

        try:

            market_cap = f"₹{data.get('market_cap', 0):,}"

        except:

            market_cap = "Not Available"

        try:

            revenue = f"₹{data.get('revenue', 0):,}"

        except:

            revenue = "Not Available"

        try:

            pe_ratio = round(
                float(
                    data.get(
                        "pe_ratio",
                        0
                    )
                ),
                2
            )

        except:

            pe_ratio = "Not Available"

        try:

            profit_margin = round(

                float(
                    data.get(
                        "profit_margin",
                        0
                    )
                ) * 100,

                2

            )

            profit_margin = f"{profit_margin}%"

        except:

            profit_margin = "Not Available"

        financial_summary.append(

            f"""
Company: {company}
Market Cap: {market_cap}
Revenue: {revenue}
PE Ratio: {pe_ratio}
Profit Margin: {profit_margin}
"""
        )

    financial_summary = "\n".join(
        financial_summary
    )

    print("\n")
    print("=" * 50)
    print("FINANCIAL METRICS")
    print("=" * 50)

    print(financial_summary)

    # ----------------------------------
    # Analysis Prompt
    # ----------------------------------

    prompt = f"""
You are a senior equity research analyst.

Research Findings:
{findings_text}

Financial Metrics:
{financial_summary}

Annual Report Evidence:
{rag_text}

IMPORTANT RULES:

1. Use ONLY the numbers provided in Financial Metrics.
2. Use Annual Report Evidence wherever possible.
3. Do NOT invent revenue, market size, CAGR, margins, growth rates, or forecasts.
4. If information is unavailable, write "Not Available".
5. Clearly distinguish facts from assumptions.
6. Mention company-specific insights from annual reports.
7. Highlight AI initiatives if present.

Generate the following sections:

# Executive Summary

# Key Trends

# Financial Analysis

# Opportunities

# Risks

# Future Outlook

Maximum 700 words.
"""

    print(
        f"\nAnalyzer Prompt Length: {len(prompt)}"
    )

    response = llm.invoke(
        prompt
    )

    state["analysis"] = (
        response.content
    )

    return state