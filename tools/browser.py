import requests
from bs4 import BeautifulSoup


class BrowserTool:

    def fetch_page(
        self,
        url: str
    ):

        try:

            response = requests.get(
                url,
                timeout=10
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            text = soup.get_text(
                separator=" ",
                strip=True
            )

            return text[:15000]

        except Exception:

            return ""