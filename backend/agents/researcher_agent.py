from backend.tools.tavily_tool import web_search

from backend.prompts.research_prompt import (
    RESEARCH_PROMPT
)

from backend.prompts.research_stages import (
    RESEARCH_STAGES
)

from backend.llm import llm


def research_loop(state):

    original_query = state["query"]

    findings = []

    search_history = []

    reasoning_chain = []

    current_query = original_query

    for step, stage in enumerate(RESEARCH_STAGES):

        print(f"\n{'='*60}")
        print(f"STEP {step+1}")
        print(f"STAGE: {stage}")
        print(f"SEARCH: {current_query}")

        # -----------------------------
        # Search
        # -----------------------------

        result = web_search(
            current_query
        )

        findings.append(
            result
        )

        search_history.append(
            current_query
        )

        # -----------------------------
        # Reduce Prompt Size
        # -----------------------------

        recent_history = search_history[-3:]

        recent_findings = []

        for item in findings[-2:]:

            recent_findings.append(
                str(item)[:1000]
            )

        prompt = RESEARCH_PROMPT.format(
            query=original_query,
            stage=stage,
            history=recent_history,
            findings=recent_findings
        )

        print(
            f"Prompt Length: {len(prompt)}"
        )

        # -----------------------------
        # Generate Next Query
        # -----------------------------

        try:

            next_query = (
                llm.invoke(prompt)
                .content
                .strip()
                .replace('"', '')
            )

        except Exception as e:

            print(
                f"Research Error: {e}"
            )

            break

        reasoning_chain.append({

            "step": step + 1,

            "stage": stage,

            "search": current_query,

            "next_search": next_query

        })

        current_query = next_query

    state["findings"] = findings

    state["search_history"] = (
        search_history
    )

    state["reasoning_chain"] = (
        reasoning_chain
    )

    return state