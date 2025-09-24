from google.adk.agents import LoopAgent

from ..critic_agent.agent import critic_agent
from ..editor_agent.agent import editor_agent

refinement_loop = LoopAgent(
    name="RefinementLoop",
    description="""
    A loop agent that facilitates the iterative refinement of the story. It repeatedly cycles 
    between the critic and editor agents to improve the draft until it is complete or the 
    maximum number of iterations is reached.
    """,
    sub_agents=[
        critic_agent,
        editor_agent,
    ],
    max_iterations=5
)
