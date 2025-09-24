import logging

from a2a.server.agent_execution import AgentExecutor
from a2a.utils.errors import ServerError
from google.adk import Runner

from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.types import (
    Task,
    Part,
    TextPart,
    UnsupportedOperationError,
)

from a2a.utils import (
    completed_task,
    new_artifact,
)

from agent import StorytellerAgent

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class StorytellerAgentExecutor(AgentExecutor):

    def __init__(self, runner: Runner = None):
        super().__init__()
        self.agent = StorytellerAgent()
        self.runner = runner
        self._running_sessions = {}

    async def execute(
        self,
        context: RequestContext,
        event_queue: EventQueue,
    ) -> None:
        query = context.get_user_input()
        try:
            result = await self.agent.invoke(query, context.context_id)
            logger.info(f"Agent Result ===> {result}")

            parts = [Part(root=TextPart(text=str(result)))]

            await event_queue.enqueue_event(
                completed_task(
                    context.task_id,
                    context.context_id,
                    [new_artifact(parts, f"storyteller_story_{context.task_id}")],
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