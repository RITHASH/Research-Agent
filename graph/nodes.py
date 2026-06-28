from agents.planner import planner_agent

from schemas.state import AgentState

from agents.search_agent import search_agent

from agents.research_agent import research_agent

from agents.synthesizer import synthesizer_agent

from agents.critic import critic_agent

from agents.report_agent import report_agent

from agents.memory_agent import memory_agent

from agents.browser_agent import browser_agent

from agents.boss_agent import boss_agent


from agents.reranker_agent import (
    reranker_agent
)

from agents.query_expander import (
    query_expander_agent
)

from agents.tool_manager import (
    tool_manager_agent
)

from agents.tool_selector import (
    tool_selector_agent
)

from agents.task_allocator import (
    task_allocator_agent
)

from agents.worker_tool_selector import (
    worker_tool_selector_agent
)

from agents.graph_memory_agent import (
    graph_memory_agent
)

from agents.entity_extractor import (
    entity_extractor_agent
)

from agents.quality_agent import (
    quality_agent
)

from agents.research_judge import (
    research_judge_agent
)

from agents.tool_execution_agent import (
    tool_execution_agent
)

from agents.tool_routing_agent import (
    tool_routing_agent
)

from agents.source_fusion_agent import (
    source_fusion_agent
)

def planner_node(state: AgentState):

    query = state["query"]

    state["plan"] = [
        f"Research topic: {query}",
        "Search web",
        "Generate report"
    ]

    return state

def planner_node(state):

    return planner_agent(state)

async def search_node(
    state
):

    return await search_agent(
        state
    )

def research_node(state):

    return research_agent(state)

def synthesizer_node(state):

    return synthesizer_agent(state)

def critic_node(state):

    return critic_agent(state)

def report_node(state):

    return report_agent(state)

async def memory_node(
    state
):

    return await memory_agent(
        state
    )

def browser_node(state):

    return browser_agent(state)

async def browser_node(
    state
):

    return await browser_agent(
        state
    )

def query_expander_node(state):

    return query_expander_agent(state)

def boss_node(state):

    return boss_agent(state)

def tool_manager_node(state):

    return tool_manager_agent(
        state
    )

def tool_selector_node(state):

    return tool_selector_agent(
        state
    )

def task_allocator_node(state):

    return task_allocator_agent(
        state
    )

def worker_tool_selector_node(
    state
):

    return (
        worker_tool_selector_agent(
            state
        )
    )

def graph_memory_node(state):

    return graph_memory_agent(
        state
    )

def entity_extractor_node(
    state
):

    return entity_extractor_agent(
        state
    )

def quality_node(state):

    return quality_agent(
        state
    )

def research_judge_node(
    state
):

    return (
        research_judge_agent(
            state
        )
    )

async def tool_execution_node(
    state
):

    return await (
        tool_execution_agent(
            state
        )
    )
    
def tool_routing_node(
    state
):

    return (
        tool_routing_agent(
            state
        )
    )

def source_fusion_node(
    state
):

    return (
        source_fusion_agent(
            state
        )
    )