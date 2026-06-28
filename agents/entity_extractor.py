from llm.llm_client import LLMClient

llm = LLMClient()


def entity_extractor_agent(state):

    notes = state[
        "research_notes"
    ]

    entities = []

    for task, content in (
        notes.items()
    ):

        prompt = f"""
Extract entities and relationships.

Text:

{content}

Return format:

ENTITY|name

RELATION|source|relation|target
"""

        result = llm.invoke(
            prompt
        )

        entities.append(result)

    state[
        "entity_extractions"
    ] = entities

    return state