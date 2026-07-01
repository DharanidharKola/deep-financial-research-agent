from backend.llm import llm

def create_plan(state):

    query = state["query"]

    prompt = f"""
    Create a research plan.

    Query:
    {query}

    Include:

    Market Analysis

    Financial Analysis

    Competitor Analysis

    Risks

    Opportunities

    Future Outlook

    Return as numbered list.
    """

    plan = llm.invoke(prompt)

    state["research_plan"] = (
        plan.content
    )

    return state