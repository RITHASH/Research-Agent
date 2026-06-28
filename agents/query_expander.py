from llm.llm_client import LLMClient

llm = LLMClient()


def query_expander_agent(state):

    query = state["query"]

    prompt = f"""
You are a research strategist.

Generate 5 search queries that would help
research this topic thoroughly.

Topic:

{query}

Return one query per line.
"""

    response = llm.invoke(prompt)

    queries = []

    for line in response.split("\n"):

        line = line.strip()

        if line:

            queries.append(line)

    state["search_queries"] = queries

    return state