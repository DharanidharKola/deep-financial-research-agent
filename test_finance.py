from backend.tools.finance_tool import (
    get_company_metrics
)

data = get_company_metrics(
    "INFY.NS"
)

print(data)