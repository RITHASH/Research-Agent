def select_agent(task):

    task_lower = task.lower()

    if any(
        keyword in task_lower
        for keyword in [
            "paper",
            "research",
            "scientific",
            "study"
        ]
    ):

        return "academic"

    if any(
        keyword in task_lower
        for keyword in [
            "market",
            "startup",
            "company",
            "funding"
        ]
    ):

        return "market"

    return "web"