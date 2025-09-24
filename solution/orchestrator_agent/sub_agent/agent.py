import logging
from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

from .a2a_image_generator import image_generator_agent
from .image_loader import image_loader_agent
from .a2a_story_teller import story_teller_agent


from config import TOOLBOX_ENDPOINT, MODEL_GEMINI
from google.adk.tools import AgentTool
from .prompt import PROMPT

logger = logging.getLogger(__name__)

# Convert specialized agents into AgentTools
image_loader_tool = AgentTool(agent=image_loader_agent)
image_generator_tool = AgentTool(agent=image_generator_agent)
story_teller_tool = AgentTool(agent=story_teller_agent)


toolbox = ToolboxSyncClient(TOOLBOX_ENDPOINT)
save_story = toolbox.load_tool("insert-story")
logger.info(f"Loaded save_story tool: {save_story}")


root_agent = Agent(
    model=MODEL_GEMINI,
    name="Orchestrator",
    description="Agent that will help to create story",
    instruction=PROMPT,
    tools=[image_loader_tool, image_generator_tool, story_teller_tool, save_story],
)
