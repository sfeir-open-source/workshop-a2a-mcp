import logging
from google.adk.tools import ToolContext

logger = logging.getLogger(__name__)


def exit_loop(tool_context: ToolContext):
    logger.debug(f"[Tool Call] exit_loop triggered by {tool_context.agent_name}")
    tool_context.actions.escalate = True
    return {}
 