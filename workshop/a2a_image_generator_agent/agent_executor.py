import logging
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue

from a2a.types import (
    Part,
    Task,
    TextPart,
    UnsupportedOperationError,
)
from a2a.utils import (
    completed_task,
    new_artifact,
)
from a2a.utils.errors import ServerError
from agent import ImageGeneratorAgent

logger = logging.getLogger(__name__)


class ImageGeneratorAgentExecutor(AgentExecutor):
    """Image Generator AgentExecutor."""

    def __init__(self):
        self.agent = ImageGeneratorAgent()

    async def execute(
        self,
        context: RequestContext,
        event_queue: EventQueue,
    ) -> None:
        query = context.get_user_input()
        try:
            result = self.agent.invoke(query, context.context_id)
            logger.info(f"Agent Result ===> {result}")

            parts = [Part(root=TextPart(text=str(result)))]

            await event_queue.enqueue_event(
                completed_task(
                    context.task_id,
                    context.context_id,
                    [new_artifact(parts, f"images_story_{context.task_id}")],
                    [context.message],
                )
            )

        except Exception as e:
            logger.error("Error invoking agent: %s", e)
            raise ServerError(error=ValueError(f"Error invoking agent: {e}")) from e

    async def cancel(
        self, request: RequestContext, event_queue: EventQueue
    ) -> Task | None:
        raise ServerError(error=UnsupportedOperationError())
