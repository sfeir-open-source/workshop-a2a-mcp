import logging
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from constants import COMPLETION_PHRASE
from storyteller_agent.agent import get_agent
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class StorytellerAgent:
    """Storyteller agent that uses the existing ADK-based sequential agent pipeline."""
    
    SUPPORTED_CONTENT_TYPES = ["text/plain", "text"]
    SUPPORTED_CONTENT_TYPES_OUTPUT = ["text/plain", "application/json"]

    def __init__(self):
        # Initialize the session service
        self.session_service = InMemorySessionService()
        # Initialize the Runner for ADK agent execution
        self.runner = Runner(
            app_name="a2a-storyteller-agent",
            agent=get_agent(),
            session_service=self.session_service
        )

    async def invoke(self, query, sessionId) -> str:
        """Invoke the storyteller agent with the given query and session ID."""
        try:
            # Create a session for this request
            user_id = "user_123"  # You can make this configurable
            session = await self.session_service.create_session(
                app_name="a2a-storyteller-agent",
                user_id=user_id,
                session_id=sessionId
            )
            
            # Format the query as a Content object
            content = types.Content(role='user', parts=[types.Part(text=query)])
            
            # Use the Runner to execute the ADK agent
            events = self.runner.run(
                user_id=user_id,
                session_id=sessionId,
                new_message=content
            )
            
            # Process the agent's response - collect all events and get the final result
            response_text = ""
            all_events = list(events)  # Convert generator to list to process all events
                         
            # Get the last event that has content (which should be from the final agent)
            for event in reversed(all_events):
                if hasattr(event, 'content') and event.content and event.content.parts:
                    response_text = event.content.parts[0].text
                    if response_text and response_text != COMPLETION_PHRASE:
                        break
            
            return response_text if response_text else "No response received from agent"
        except Exception as e:
            return f"Error processing story request: {str(e)}"


if __name__ == "__main__":
    agent = StorytellerAgent()
    result = agent.invoke("A story about a brave knight on a quest", sessionId="test_agent")
    logger.info(result)