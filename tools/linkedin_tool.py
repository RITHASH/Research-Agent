import os

from linkedin_api import Linkedin

from tools.base_tool import (
    BaseTool
)


class LinkedInTool(
    BaseTool
):

    def execute(
        self,
        query
    ):

        api = Linkedin(
            os.getenv(
                "LINKEDIN_EMAIL"
            ),
            os.getenv(
                "LINKEDIN_PASSWORD"
            )
        )

        results = api.search_people(
            keywords=query
        )

        return results[:5]