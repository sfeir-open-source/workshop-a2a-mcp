from google.adk.agents.remote_a2a_agent import (
    RemoteA2aAgent,
    AGENT_CARD_WELL_KNOWN_PATH,
)
from config import A2A_IMAGE_GENERATION_URL


image_generator_agent = RemoteA2aAgent(
    name="image_generator_agent",
    description="Help the narator to create images to illustrate story",
    agent_card=(f"{A2A_IMAGE_GENERATION_URL}{AGENT_CARD_WELL_KNOWN_PATH}"),
)
