from llm.llm_client import LLMClient

llm = LLMClient()


def quality_agent(state):

    notes = state[
        "research_notes"
    ]

    scores = {}

    for task, content in (
        notes.items()
    ):

        prompt = f"""
Score this research.

Criteria:

- Accuracy
- Completeness
- Source Quality
- Insight Depth

Return only a number
from 1 to 10.

Research:

{content}
"""

        score = llm.invoke(
            prompt
        ).strip()

        try:

            score = float(
                score
            )

        except:

            score = 5.0

        scores[task] = score

    state[
        "quality_scores"
    ] = scores

    return state