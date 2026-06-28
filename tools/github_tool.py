import os
import requests

from tools.base_tool import (
    BaseTool
)


class GitHubTool(
    BaseTool
):

    def execute(
        self,
        query
    ):

        token = os.getenv(
            "GITHUB_TOKEN"
        )

        headers = {
            "Authorization":
            f"Bearer {token}"
        }

        response = requests.get(
            "https://api.github.com/search/repositories",
            params={
                "q": query,
                "per_page": 5
            },
            headers=headers
        )

        data = response.json()

        repos = []

        for repo in data.get(
            "items",
            []
        ):

            repos.append(
                {
                    "name":
                    repo["name"],

                    "url":
                    repo[
                        "html_url"
                    ],

                    "stars":
                    repo[
                        "stargazers_count"
                    ],

                    "description":
                    repo[
                        "description"
                    ]
                }
            )

        return repos