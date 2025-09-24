from a2a.types import AgentCapabilities, AgentSkill, AgentCard
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.apps import A2AStarletteApplication
from a2a.server.tasks import InMemoryTaskStore
import uvicorn
import logging
import click

from agent import StorytellerAgent
from agent_executor import StorytellerAgentExecutor


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.option("--host", "host", default="127.0.0.1")
@click.option("--port", "port", default=10002)
def main(host, port):
    """Entry point for the A2A + Storyteller Agent"""
    try:
        capabilities = AgentCapabilities(streaming=False)
        skill = AgentSkill(
            id="create_story",
            name="Story Creation Tool",
            description="Helps with writing stories",
            tags=["story creation"],
            examples=["What's new in Generative AI?"],
        )

        agent_card = AgentCard(
            name="Storyteller Agent",
            description="Helps with writing stories",
            url=f"http://{host}:{port}",
            version="1.0.0",
            defaultInputModes=StorytellerAgent.SUPPORTED_CONTENT_TYPES,
            defaultOutputModes=StorytellerAgent.SUPPORTED_CONTENT_TYPES_OUTPUT,
            capabilities=capabilities,
            skills=[skill],
        )

        request_handler = DefaultRequestHandler(
            agent_executor=StorytellerAgentExecutor(),
            task_store=InMemoryTaskStore(),
        )
        server = A2AStarletteApplication(
            agent_card=agent_card, http_handler=request_handler
        )

        uvicorn.run(server.build(), host=host, port=port)

        logger.info(f"Starting server on {host}:{port}")
    except Exception as e:
        logger.error(f"An error occurred during server startup: {e}")
        exit(1)


if __name__ == "__main__":
    main()
