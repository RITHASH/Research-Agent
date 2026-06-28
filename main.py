from graph.graph_builder import build_graph
from graph.state import create_initial_state


def main():

    graph = build_graph()

    state = create_initial_state(
        "Future of Quantum Computing"
    )

    result = graph.invoke(state)

    print("\nBOSS STRATEGY\n")
    print(result["boss_strategy"])

    print(
        result["worker_tools"]
    )

    print("\nFINAL REPORT\n")
    print(result["final_report"])


if __name__ == "__main__":
    main()