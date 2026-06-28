import networkx as nx


class KnowledgeGraph:

    def __init__(self):

        self.graph = nx.Graph()

    def add_relation(
        self,
        source,
        target,
        relation
    ):

        self.graph.add_edge(
            source,
            target,
            relation=relation
        )

    def get_neighbors(
        self,
        node
    ):

        if node not in self.graph:

            return []

        return list(
            self.graph.neighbors(node)
        )

    def add_entity(
        self,
        entity
    ):

        self.graph.add_node(
            entity
        )