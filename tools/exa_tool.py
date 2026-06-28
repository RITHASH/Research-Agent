import os

from exa_py import Exa

from tools.base_tool import (
    BaseTool
)


class ExaTool(
    BaseTool
):

    def execute(
        self,
        query
    ):

        exa = Exa(
            api_key=os.getenv(
                "EXA_API_KEY"
            )
        )

        search = exa.search_and_contents(
            query,
            num_results=5
        )

        results = []

        for item in search.results:

            results.append(
                {
                    "title":
                    item.title,

                    "url":
                    item.url,

                    "content":
                    item.text[:3000]
                }
            )

        return results