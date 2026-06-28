from llm.llm_client import LLMClient

llm = LLMClient()


def market_research_agent(
    task,
    content,
    memory_context
):

    prompt = f"""
You are a Market Research Specialist.

Task:

{task}

Content:

{content}

Previous Knowledge:

{memory_context}

Focus on:

- Companies
- Startups
- Funding
- Business opportunities
"""

    return llm.invoke(prompt)