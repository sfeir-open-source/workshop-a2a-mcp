from google.adk import Agent
from google.adk.tools import google_search
from constants import STATE_SEARCH_RESULTS, MODEL_GEMINI

search_agent = Agent(
    name="SearchAgent",
    description="""
    A search agent that uses the Google Search tool to gather information based on the user's query, 
    providing the foundational content for the story.
    """,
    model=MODEL_GEMINI,
    instruction="""
    You are a research assistant for a storyteller. Your goal is to use the available tools to find 
    relevant information for a story based on the user's request. The output of your research will be used 
    to write a story.
    """,
    tools=[google_search],
    output_key=STATE_SEARCH_RESULTS,
)
