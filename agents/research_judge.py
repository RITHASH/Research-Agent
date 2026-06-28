def research_judge_agent(state):

    scores = state[
        "quality_scores"
    ]

    average = (
        sum(scores.values())
        /
        max(
            len(scores),
            1
        )
    )

    state[
        "needs_more_research"
    ] = average < 7

    return state