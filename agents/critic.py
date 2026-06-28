from llm.llm_client import LLMClient

llm = LLMClient()


def critic_agent(state):

    report = state["draft_report"]

    prompt = f"""
You are an expert research reviewer.

Review the report.

Evaluate:

1. Accuracy
2. Completeness
3. Missing Information
4. Quality of Sources
5. Depth of Research

At the end write:

VERDICT: PASS

or

VERDICT: FAIL

Report:

{report}
"""

    critique = llm.invoke(prompt)

    state["critique"] = critique

    state["iteration_count"] += 1

    if (
        "VERDICT: FAIL" in critique
        and state["iteration_count"] < 3
    ):

        state["needs_revision"] = True

    else:

        state["needs_revision"] = False

    return state
    
