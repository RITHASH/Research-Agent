from llm.llm_client import LLMClient

llm = LLMClient()


def reranker_agent(state):

    webpage_content = state["webpage_content"]

    filtered_content = {}

    for task, pages in webpage_content.items():

        filtered_content[task] = []

        for page in pages[:5]:

            content = page["content"]

            if len(content) < 500:
                continue

            filtered_content[task].append(
                page
            )

    state["filtered_content"] = (
        filtered_content
    )

    return state