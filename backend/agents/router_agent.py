def route_query(state):

    query = state["query"].lower()

    pharma_keywords = [
        "pharma",
        "pharmaceutical",
        "drug",
        "medicine",
        "healthcare",
        "biotech",
        "cipla",
        "sun pharma",
        "dr reddy"
    ]

    if any(
        keyword in query
        for keyword in pharma_keywords
    ):

        sector = "Pharma"

    else:

        sector = "IT"

    print(
        f"\nROUTER DETECTED: [{sector}]"
    )

    state["sector"] = sector

    return state