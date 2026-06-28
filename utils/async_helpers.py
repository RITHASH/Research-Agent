import asyncio


async def run_tasks(
    tasks
):

    return await asyncio.gather(
        *tasks
    )