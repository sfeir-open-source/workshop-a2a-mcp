from google.adk.agents import SequentialAgent

from .draft_writer_agent.agent import draft_writer_agent
from .refinement_loop.agent import refinement_loop
from .search_agent.agent import search_agent

root_agent = SequentialAgent(
    name="IterativeStoryWritingPipeline",
    description="A sequential agent that orchestrates the story writing process by first searching for information, then writing a draft, and finally entering a refinement loop to iteratively improve the story.",
    sub_agents=[
        search_agent,
        draft_writer_agent,
        refinement_loop
    ],

)

def get_agent():
    return root_agent
