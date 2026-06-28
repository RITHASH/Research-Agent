from llm.llm_client import LLMClient

llm = LLMClient()


def web_research_agent(
    task,
    content,
    memory_context
):

    prompt = f"""
You are a Web Research Specialist.

Task:

{task}

Content:

{content}

Previous Knowledge:

{memory_context}

Focus on:

- News
- Trends
- Industry developments
- Current events
"""

    return llm.invoke(prompt)