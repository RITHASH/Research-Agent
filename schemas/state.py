from typing import List, Optional
from typing_extensions import TypedDict


class AgentState(TypedDict):

    query: str

    plan: List[str]
    
    subtasks: List[str]

    search_results: dict

    research_notes: dict

    draft_report: str

    final_report: str

    critique: str

    iteration_count: int

    memory_context: list

    citations: list
    
    webpage_content: dict

    filtered_content: dict
    
    needs_revision: bool

    search_queries: list

    boss_strategy: str

    completed_tasks: list
    
    research_progress: dict

    additional_tasks: list

    available_tools: list

    tool_results: dict

    selected_tools: list
    
    task_assignments: dict

    worker_tools: dict

    knowledge_graph_updates: list

    entity_extractions: list

    quality_scores: dict

    needs_more_research: bool

    tool_execution_results: dict

    github_results: dict

    reddit_results: dict

    youtube_results: dict

    exa_results: dict

    twitter_results: dict

    rss_results: dict

    linkedin_results: dict

    unified_research: dict