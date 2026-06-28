import asyncio

from memory.memory_manager import (
    MemoryManager
)

memory = MemoryManager()


async def memory_agent(
    state
):

    query = state["query"]

    results = (
        memory.retrieve(
            query
        )
    )

    state[
        "memory_context"
    ] = results

    return state