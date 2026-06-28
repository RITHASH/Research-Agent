import asyncio

from tools.tool_executor import (
    ToolExecutor
)

executor = ToolExecutor()


async def execute_tool(
    task,
    tool
):

    try:

        output = (
            executor.execute(
                tool,
                task
            )
        )

        return (
            task,
            tool,
            output
        )

    except Exception:

        return (
            task,
            tool,
            []
        )


async def tool_execution_agent(
    state
):

    worker_tools = state[
        "worker_tools"
    ]

    execution_tasks = []

    for task, tools in (
        worker_tools.items()
    ):

        for tool in tools:

            execution_tasks.append(
                execute_tool(
                    task,
                    tool
                )
            )

    results = await asyncio.gather(
        *execution_tasks
    )

    tool_results = {}

    for task, tool, output in (
        results
    ):

        tool_results.setdefault(
            task,
            {}
        )[tool] = output

    state[
        "tool_execution_results"
    ] = tool_results

    return state