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
        # TODO: Create AgentSkill for story creation
        # Define skill with id, name, description, tags, and examples.
        skill = 

        # TODO: Create AgentCard for storyteller agent
        # Define agent card with name, description, url, version, input/output modes, capabilities, and skills.
        agent_card = 

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
