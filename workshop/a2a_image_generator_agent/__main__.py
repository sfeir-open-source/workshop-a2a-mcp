from a2a.types import AgentCapabilities, AgentSkill, AgentCard
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.apps import A2AStarletteApplication
from a2a.server.tasks import InMemoryTaskStore
from agent import ImageGeneratorAgent
from agent_executor import ImageGeneratorAgentExecutor
import uvicorn
import logging
import click


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.option("--host", "host", default="127.0.0.1")
@click.option("--port", "port", default=10001)
def main(host, port):
    """Entry point for the A2A + CrewAI Image generator Agent"""
    try:
        capabilities = AgentCapabilities(streaming=False)
        skill = AgentSkill(
            id="create_story_image",
            name="Image Creation Tool",
            description="Helps with creating image ",
            tags=["image creation"],
            examples=["I want an image of super heros with keyboard"],
        )

        agent_card = AgentCard(
            name="Story image generator",
            description="Helps with creating illustration for story",
            url=f"http://{host}:{port}",
            version="1.0.0",
            default_input_modes=ImageGeneratorAgent.SUPPORTED_CONTENT_TYPES,
            default_output_modes=ImageGeneratorAgent.SUPPORTED_CONTENT_TYPES_OUTPUT,
            capabilities=capabilities,
            skills=[skill],
        )

        request_handler = DefaultRequestHandler(
            agent_executor=ImageGeneratorAgentExecutor(),
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
