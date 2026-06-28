from llm.llm_client import LLMClient

llm = LLMClient()


def planner_agent(state):

    query = state["query"]

    prompt = f"""
You are an expert research planner.

Create a research plan for the topic below.

Return ONLY a numbered list.

Topic:

{query}
"""

    response = llm.invoke(prompt)

    lines = []

    for line in response.split("\n"):

        line = line.strip()

        if line:
            lines.append(line)

    state["plan"] = lines

    state["subtasks"] = lines

    return state