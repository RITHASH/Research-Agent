from llm.llm_client import LLMClient

llm = LLMClient()


def boss_agent(state):

    query = state["query"]

    completed = state.get(
        "completed_tasks",
        []
    )

    progress_report = (
        "\n".join(completed)
        if completed
        else "No tasks completed yet."
    )

    prompt = f"""
You are the Research Manager.

Research Goal:

{query}

Completed Research Areas:

{progress_report}

Identify:

1. Missing areas
2. Knowledge gaps
3. Additional research needed

Return ONLY a list of new tasks.
"""

    response = llm.invoke(prompt)

    tasks = []

    for line in response.split("\n"):

        line = line.strip()

        if line:

            tasks.append(line)

    existing_tasks = set(
        state["completed_tasks"]
    )

    new_tasks = []

    for task in tasks:

        if task not in existing_tasks:

            new_tasks.append(task)

    state["additional_tasks"] = new_tasks

    state["boss_strategy"] = response

    return state