from google.adk.agents.remote_a2a_agent import (
    RemoteA2aAgent,
    AGENT_CARD_WELL_KNOWN_PATH,
)
from config import A2A_STORYTELLER_URL

story_teller_agent = RemoteA2aAgent(
    name="story_generator_agent",
    description="Help the nuser to create a story",
    agent_card=(f"{A2A_STORYTELLER_URL}{AGENT_CARD_WELL_KNOWN_PATH}"),
)
