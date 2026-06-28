from youtubesearchpython import (
    VideosSearch
)

from tools.base_tool import (
    BaseTool
)


class YouTubeTool(
    BaseTool
):

    def execute(
        self,
        query
    ):

        search = VideosSearch(
            query,
            limit=5
        )

        results = []

        for video in (
            search.result()[
                "result"
            ]
        ):

            results.append(
                {
                    "title":
                    video["title"],

                    "url":
                    video["link"],

                    "channel":
                    video["channel"][
                        "name"
                    ]
                }
            )

        return results