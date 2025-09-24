from google.adk import Agent

from .tools import load_image_data
from config import MODEL_GEMINI

image_loader_agent = Agent(
    model=MODEL_GEMINI,
    name="image_loader",
    description="Agent that will get image from cloudStorage and load it as an artifact ",
    instruction="""You are a helpful assistant that load image from cloud storage and store it as an atrifact.
     You load image with the load_image_data tool and send back the artifact with the name of the file
     """,
    tools=[load_image_data],
    output_key="image",
)
