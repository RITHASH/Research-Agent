from llm.llm_client import LLMClient

llm = LLMClient()


def synthesizer_agent(state):

    notes = state["research_notes"]

    combined_notes = ""

    for task, content in notes.items():

        combined_notes += f"""

# {task}

{content}

"""

    prompt = f"""
Create a professional research report.

Research Material:

{combined_notes}

Structure:

# Executive Summary

# Key Findings

# Detailed Analysis

# Conclusion
"""

    report = llm.invoke(prompt)

    state["draft_report"] = report

    return state
