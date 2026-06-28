from memory.knowledge_graph import (
    KnowledgeGraph
)

kg = KnowledgeGraph()


def graph_memory_agent(state):

    updates = []

    for extraction in (
        state["entity_extractions"]
    ):

        for line in extraction.split(
            "\n"
        ):

            line = line.strip()

            if not line:
                continue

            parts = line.split("|")

            if not parts:
                continue

            try:

                if parts[0] == "ENTITY":

                    entity = parts[1]

                    kg.add_entity(
                        entity
                    )

                    updates.append(
                        {
                            "type": "entity",
                            "entity": entity
                        }
                    )

                elif parts[0] == "RELATION":

                    source = parts[1]
                    relation = parts[2]
                    target = parts[3]

                    kg.add_relation(
                        source,
                        target,
                        relation
                    )

                    updates.append(
                        {
                            "type": "relation",
                            "source": source,
                            "relation": relation,
                            "target": target
                        }
                    )

            except Exception:

                continue

    state[
        "knowledge_graph_updates"
    ] = updates

    return state