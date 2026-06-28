from llm.llm_client import LLMClient

llm = LLMClient()


def worker_tool_selector_agent(state):

    assignments = state[
        "task_assignments"
    ]

    available_tools = state[
        "available_tools"
    ]

    worker_tools = {}

    for task, worker in (
        assignments.items()
    ):

        prompt = f"""
You are an expert tool planner.

Worker:

{worker}

Available Tools:

{available_tools}

Choose the best tools.

Return one tool per line.
"""

        response = llm.invoke(
            prompt
        )

        tools = []

        for line in response.split(
            "\n"
        ):

            line = line.strip()

            if line:

                tools.append(
                    line
                )

        worker_tools[
            task
        ] = tools

    state["worker_tools"] = (
        worker_tools
    )

    return state