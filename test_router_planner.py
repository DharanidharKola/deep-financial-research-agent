from backend.agents.router_agent import route_query
from backend.agents.planner_agent import create_plan

state = {
    "query": "Analyze biosimilars opportunities in Indian pharma sector"
}

print("=" * 50)
print("INITIAL STATE")
print(state)

# Router
state = route_query(state)

print("\n" + "=" * 50)
print("ROUTER OUTPUT")
print(state["sector"])

# Planner
state = create_plan(state)

print("\n" + "=" * 50)
print("RESEARCH PLAN")
print(state["research_plan"])