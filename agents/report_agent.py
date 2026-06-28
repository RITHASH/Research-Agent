from llm.llm_client import LLMClient
from memory.memory_manager import MemoryManager

llm = LLMClient()
memory = MemoryManager()


def report_agent(state):

    draft_report = state["draft_report"]

    critique = state["critique"]

    prompt = f"""
You are a professional research editor.

You are given:

1. A draft report.
2. Review feedback.

Your task:

- Improve the report.
- Fix weaknesses.
- Add missing information where possible.
- Improve clarity.
- Improve structure.
- Improve conclusions.
- Ensure professional quality.

Return ONLY the improved report.

Draft Report:

{draft_report}

Review Feedback:

{critique}
"""

    final_report = llm.invoke(prompt)

    references = "\n\n# References\n\n"

    for citation in state["citations"]:

        references += (
            f"- {citation['title']}: "
            f"{citation['url']}\n"
        )

    final_report += references

    state["final_report"] = final_report

    memory.save_research(
        topic=state["query"],
        content=final_report
    )

    return state