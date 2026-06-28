def source_fusion_agent(
    state
):

    unified = {}

    sources = [
        "github_results",
        "reddit_results",
        "youtube_results",
        "exa_results",
        "twitter_results",
        "rss_results",
        "linkedin_results"
    ]

    tasks = set()

    for source in sources:

        tasks.update(
            state.get(
                source,
                {}
            ).keys()
        )

    for task in tasks:

        unified[task] = []

        for source in sources:

            data = state.get(
                source,
                {}
            )

            if task in data:

                unified[
                    task
                ].extend(
                    data[task]
                )

    state[
        "unified_research"
    ] = unified

    return state