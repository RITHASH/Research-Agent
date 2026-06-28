import asyncio

from tools.browser import (
    BrowserTool
)

browser = BrowserTool()


async def fetch_page(
    task,
    url
):

    content = (
        browser.fetch_page(
            url
        )
    )

    return (
        task,
        {
            "url": url,
            "content": content
        }
    )


async def browser_agent(
    state
):

    search_results = (
        state["search_results"]
    )

    webpage_content = {}

    tasks = []

    for task, results in (
        search_results.items()
    ):

        for result in results:

            url = result.get(
                "url",
                ""
            )

            if not url:
                continue

            tasks.append(
                fetch_page(
                    task,
                    url
                )
            )

    pages = await asyncio.gather(
        *tasks
    )

    for task, page in pages:

        webpage_content.setdefault(
            task,
            []
        ).append(page)

    state[
        "webpage_content"
    ] = webpage_content

    return state