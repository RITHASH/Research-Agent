from agents.web_research_agent import (
    web_research_agent
)

from agents.academic_research_agent import (
    academic_research_agent
)

from agents.market_research_agent import (
    market_research_agent
)

from agents.knowledge_research_agent import (
    knowledge_research_agent
)


def research_agent(state):

    webpage_content = state["filtered_content"]

    unified_research = state.get(
        "unified_research",
        {}
    )

    memory_context = "\n\n".join(
        state["memory_context"]
    )

    notes = {}

    citations = []

    for task, pages in webpage_content.items():

        worker = state[
            "task_assignments"
        ].get(
            task,
            "web"
        )

        context = ""

        if task in unified_research:

            context += f"""
Unified Research Sources:

{unified_research[task]}

--------------------------------
"""

        for page in pages:

            url = page.get(
                "url",
                ""
            )

            content = page.get(
                "content",
                ""
            )

            citations.append(
                {
                    "title": task,
                    "url": url
                }
            )

            context += f"""
URL:
{url}

Content:
{content}

--------------------------------
"""

        if worker == "academic":

            analysis = academic_research_agent(
                task,
                context,
                memory_context
            )

        elif worker == "market":

            analysis = market_research_agent(
                task,
                context,
                memory_context
            )

        elif worker == "knowledge":

            analysis = knowledge_research_agent(
                task,
                context,
                memory_context
            )

        else:

            analysis = web_research_agent(
                task,
                context,
                memory_context
            )

        notes[task] = analysis

        state["completed_tasks"].append(
            task
        )

        state["research_progress"][task] = {
            "status": "completed",
            "worker": worker
        }

    state["research_notes"] = notes

    state["citations"] = citations

    return state