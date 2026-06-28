import asyncio

from tools.web_search import (
    WebSearchTool
)

search_tool = WebSearchTool()


async def search_task(
    query
):

    try:

        results = (
            search_tool.search(
                query=query,
                max_results=5
            )
        )

        return (
            query,
            results
        )

    except Exception:

        return (
            query,
            []
        )


async def search_agent(
    state
):

    tasks = (
        state["subtasks"]
        +
        state["search_queries"]
        +
        state["additional_tasks"]
    )

    search_tasks = [

        search_task(
            task
        )

        for task in tasks
    ]

    results = await asyncio.gather(
        *search_tasks
    )

    state[
        "search_results"
    ] = dict(results)

    return state