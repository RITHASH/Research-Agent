from llm.llm_client import LLMClient

llm = LLMClient()


def academic_research_agent(
    task,
    content,
    memory_context
):

    prompt = f"""
You are an Academic Research Specialist.

Task:

{task}

Content:

{content}

Previous Knowledge:

{memory_context}

Focus on:

- Research papers
- Scientific evidence
- Technical findings
- Methodologies
"""

    return llm.invoke(prompt)