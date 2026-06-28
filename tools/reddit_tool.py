import os
import praw

from tools.base_tool import (
    BaseTool
)


class RedditTool(
    BaseTool
):

    def execute(
        self,
        query
    ):

        reddit = praw.Reddit(
            client_id=os.getenv(
                "REDDIT_CLIENT_ID"
            ),
            client_secret=os.getenv(
                "REDDIT_CLIENT_SECRET"
            ),
            user_agent=os.getenv(
                "REDDIT_USER_AGENT"
            )
        )

        results = []

        for post in reddit.subreddit(
            "all"
        ).search(
            query,
            limit=5
        ):

            results.append(
                {
                    "title":
                    post.title,

                    "url":
                    post.url,

                    "score":
                    post.score
                }
            )

        return results