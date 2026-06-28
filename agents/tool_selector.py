from llm.llm_client import LLMClient

llm = LLMClient()


def tool_selector_agent(state):

    query = state["query"]

    available_tools = state[
        "available_tools"
    ]

    prompt = f"""
You are an expert research manager.

Research Goal:

{query}

Available Tools:

{available_tools}

Select the most useful tools.

Return only tool names,
one per line.
"""

    response = llm.invoke(prompt)

    selected_tools = []

    for line in response.split("\n"):

        line = line.strip()

        if line:

            selected_tools.append(
                line
            )

    state["selected_tools"] = (
        selected_tools
    )

    return state