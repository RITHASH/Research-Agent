from tools.tool_registry import (
    ToolRegistry
)

registry = ToolRegistry()


class ToolExecutor:

    def execute(
        self,
        tool_name,
        query
    ):

        tool = registry.get(
            tool_name
        )

        if tool is None:

            return []

        return tool.execute(
            query
        )