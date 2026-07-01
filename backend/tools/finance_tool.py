import yfinance as yf


def get_company_metrics(ticker):

    stock = yf.Ticker(ticker)

    info = stock.info

    return {

        "company": info.get("longName"),

        "market_cap": info.get("marketCap"),

        "current_price": info.get("currentPrice"),

        "pe_ratio": info.get("trailingPE"),

        "revenue": info.get("totalRevenue"),

        "profit_margin": info.get("profitMargins"),

        "sector": info.get("sector")
    }

def calculate_revenue_growth(
    current,
    previous
):

    if not previous:

        return None

    return round(

        (
            (current - previous)

            / previous
        ) * 100,

        2
    )