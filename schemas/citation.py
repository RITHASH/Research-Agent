from pydantic import BaseModel


class Citation(BaseModel):

    source_title: str

    source_url: str