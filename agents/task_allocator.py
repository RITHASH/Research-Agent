from llm.llm_client import LLMClient

llm = LLMClient()


def task_allocator_agent(state):

    tasks = (
        state["subtasks"]
        +
        state["search_queries"]
        +
        state["additional_tasks"]
    )

    assignments = {}

    workers = [
        "web",
        "academic",
        "market",
        "knowledge"
    ]

    for task in tasks:

        prompt = f"""
You are a research manager.

Task:

{task}

Workers:

web
academic
market
knowledge

Choose the best worker.

Return only:

web

or

academic

or

market

or

knowledge
"""

        worker = (
            llm.invoke(prompt)
            .strip()
            .lower()
        )

        if worker not in workers:

            worker = "web"

        assignments[task] = worker

    state["task_assignments"] = (
        assignments
    )

    return state