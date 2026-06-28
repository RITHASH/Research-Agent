import feedparser

from tools.base_tool import (
    BaseTool
)


class RSSTool(
    BaseTool
):

    def execute(
        self,
        query
    ):

        feeds = [
            "https://news.google.com/rss/search?q=" + query
        ]

        results = []

        for feed_url in feeds:

            feed = feedparser.parse(
                feed_url
            )

            for entry in (
                feed.entries[:5]
            ):

                results.append(
                    {
                        "title":
                        entry.title,

                        "url":
                        entry.link
                    }
                )

        return results