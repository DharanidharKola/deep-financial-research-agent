from backend.graph.workflow import graph

initial_state = {

    "query":
    "Analyze Indian pharma services sector outlook",

    "sector": "",

    "approved": True,

    "research_plan": "",

    "current_query": "",

    "search_history": [],

    "findings": [],

    "reasoning_chain": [],

    "financial_metrics": {},

    "rag_context": [],

    "analysis": "",

    "final_report": ""
}

result = graph.invoke(
    initial_state
)

print("\n")
print("=" * 60)
print("FINAL REPORT")
print("=" * 60)

print(result["final_report"])

print("\n")
print("=" * 60)
print("SOURCE DOCUMENTS")
print("=" * 60)

for source in result.get(
    "source_documents", []
):
    print(source)