from llm.llm_client import LLMClient

llm = LLMClient()


def knowledge_research_agent(
    task,
    content,
    memory_context
):

    prompt = f"""
You are a Knowledge Base Specialist.

Task:

{task}

Content:

{content}

Previous Knowledge:

{memory_context}

Focus on:

- Internal documents
- Stored knowledge
- Historical information
"""

    return llm.invoke(prompt)