from backend.agents.financial_agent import (
    collect_financials
)

state = {

    "sector": "IT"
}

result = collect_financials(state)

for company, metrics in result[
    "financial_metrics"
].items():

    print(company)

    print(metrics)

    print("-" * 50)