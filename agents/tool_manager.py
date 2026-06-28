from tools.tool_registry import (
    ToolRegistry
)

from tools.github_tool import (
    GitHubTool
)

from tools.reddit_tool import (
    RedditTool
)

from tools.youtube_tool import (
    YouTubeTool
)

from tools.exa_tool import (
    ExaTool
)

from tools.twitter_tool import (
    TwitterTool
)

from tools.rss_tool import (
    RSSTool
)

from tools.linkedin_tool import (
    LinkedInTool
)

registry = ToolRegistry()

registry.register(
    "github",
    GitHubTool()
)

registry.register(
    "reddit",
    RedditTool()
)

registry.register(
    "youtube",
    YouTubeTool()
)

registry.register(
    "exa",
    ExaTool()
)

registry.register(
    "twitter",
    TwitterTool()
)

registry.register(
    "rss",
    RSSTool()
)

registry.register(
    "linkedin",
    LinkedInTool()
)

def tool_manager_agent(state):

    state["available_tools"] = (
        registry.available_tools()
    )

    return state
