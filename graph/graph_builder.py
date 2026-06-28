from langgraph.graph import StateGraph

from schemas.state import AgentState

from graph.nodes import (
    planner_node,
    memory_node,
    search_node,
    browser_node,
    reranker_node,
    research_node,
    synthesizer_node,
    critic_node,
    report_node,
    query_expander_node,
    boss_node,
    tool_manager_node,
    tool_selector_node,
    task_allocator_node,
    worker_tool_selector_node,
    graph_memory_node,
    entity_extractor_node,
    quality_node,
    research_judge_node,
    tool_execution_node,
    tool_routing_node,
    source_fusion_node
)


def critique_router(state):

    if state["needs_revision"]:

        return "research"

    return "report"


def research_router(state):

    if (
        state["needs_more_research"]
        and
        state["iteration_count"] < 3
    ):

        return "research"

    return "synthesizer"


def build_graph():

    graph = StateGraph(AgentState)

    # Nodes

    graph.add_node(
        "planner",
        planner_node
    )

    graph.add_node(
        "memory",
        memory_node
    )

    graph.add_node(
        "search",
        search_node
    )

    graph.add_node(
        "browser",
        browser_node
    )

    graph.add_node(
        "reranker",
        reranker_node
    )

    graph.add_node(
        "research",
        research_node
    )

    graph.add_node(
        "synthesizer",
        synthesizer_node
    )

    graph.add_node(
        "critic",
        critic_node
    )

    graph.add_node(
        "report",
        report_node
    )

    graph.add_node(
        "query_expander",
        query_expander_node
    )

    graph.add_node(
        "boss",
        boss_node
    )

    graph.add_node(
        "tool_manager",
        tool_manager_node
    )

    graph.add_node(
        "tool_selector",
        tool_selector_node
    )

    graph.add_node(
        "task_allocator",
        task_allocator_node
    )

    graph.add_node(
        "worker_tool_selector",
        worker_tool_selector_node
    )

    graph.add_node(
        "graph_memory",
        graph_memory_node
    )

    graph.add_node(
        "entity_extractor",
        entity_extractor_node
    )

    graph.add_node(
        "quality",
        quality_node
    )

    graph.add_node(
        "research_judge",
        research_judge_node
    )

    graph.add_node(
        "tool_execution",
        tool_execution_node
    )

    graph.add_node(
        "tool_routing",
        tool_routing_node
    )

    graph.add_node(
        "source_fusion",
        source_fusion_node
    )

    # Flow

    graph.add_edge(
        "boss",
        "tool_manager"
    )

    graph.add_edge(
        "tool_manager",
        "tool_selector"
    )

    graph.add_edge(
        "tool_selector",
        "planner"
    )

    graph.add_edge(
        "planner",
        "task_allocator"
    )

    graph.add_edge(
        "task_allocator",
        "tool_routing"
    )

    graph.add_edge(
        "tool_routing",
        "worker_tool_selector"
    )

    graph.add_edge(
        "worker_tool_selector",
        "tool_execution"
    )

    graph.add_edge(
        "tool_execution",
        "source_fusion"
    )

    graph.add_edge(
        "source_fusion",
        "query_expander"
    )

    graph.add_edge(
        "query_expander",
        "memory"
    )

    graph.add_edge(
        "query_expander",
        "search"
    )

    graph.add_edge(
        "memory",
        "reranker"
    )

    graph.add_edge(
        "search",
        "browser"
    )

    graph.add_edge(
        "browser",
        "reranker"
    )

    graph.add_edge(
        "reranker",
        "research"
    )

    graph.add_edge(
        "research",
        "entity_extractor"
    )

    graph.add_edge(
        "entity_extractor",
        "graph_memory"
    )

    graph.add_edge(
        "graph_memory",
        "quality"
    )

    graph.add_edge(
        "quality",
        "research_judge"
    )

    graph.add_conditional_edges(
        "research_judge",
        research_router
    )

    graph.add_edge(
        "synthesizer",
        "critic"
    )

    graph.add_conditional_edges(
        "critic",
        critique_router
    )

    graph.set_entry_point(
        "boss"
    )

    graph.set_finish_point(
        "report"
    )

    return graph.compile()