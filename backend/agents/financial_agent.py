from backend.tools.finance_tool import (
    get_company_metrics
)

from backend.sector_agents.it_agent import (
    IT_COMPANIES
)

from backend.sector_agents.pharma_agent import (
    PHARMA_COMPANIES
)


def collect_financials(state):

    sector = state["sector"]

    metrics = {}

    if sector == "IT":

        companies = IT_COMPANIES

    elif sector == "Pharma":

        companies = PHARMA_COMPANIES

    else:

        companies = {}

    for company, ticker in companies.items():

        try:

            metrics[company] = (
                get_company_metrics(ticker)
            )

        except Exception as e:

            print(
                f"Error: {company}"
            )

    state["financial_metrics"] = metrics

    return state