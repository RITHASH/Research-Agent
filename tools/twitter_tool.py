import os

import tweepy

from tools.base_tool import (
    BaseTool
)


class TwitterTool(
    BaseTool
):

    def execute(
        self,
        query
    ):

        client = tweepy.Client(
            bearer_token=os.getenv(
                "TWITTER_BEARER_TOKEN"
            )
        )

        tweets = client.search_recent_tweets(
            query=query,
            max_results=10
        )

        results = []

        if tweets.data:

            for tweet in tweets.data:

                results.append(
                    {
                        "text":
                        tweet.text
                    }
                )

        return results