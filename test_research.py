from backend.agents.researcher_agent import (
    research_loop
)

state = {

    "query":
    "Analyze Indian IT services sector outlook"

}

result = research_loop(state)

print("\n\n")

print("=" * 60)
print("SEARCH HISTORY")
print("=" * 60)

for search in result["search_history"]:

    print(search)

print("\n\n")

print("=" * 60)
print("RESEARCH REASONING")
print("=" * 60)

for item in result["reasoning_chain"]:

    print(
        f"""
STEP: {item['step']}
STAGE: {item['stage']}
SEARCH: {item['search']}
NEXT: {item['next_search']}
"""
    )