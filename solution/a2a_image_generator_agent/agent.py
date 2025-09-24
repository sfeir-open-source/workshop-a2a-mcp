import logging
from crewai import Agent, Crew, LLM, Task, Process
from crewai.tools import tool
from dotenv import load_dotenv
from vertexai.preview.vision_models import ImageGenerationModel
from prompts import IMAGE_GENERATOR_PROMPT, PROMPT_ENHANCEMENT_TEMPLATE
from config import GCS_IMAGE_BUCKET, MODEL_GEMINI_CREW, MODEL_IMAGEN

load_dotenv()
logger = logging.getLogger(__name__)


@tool("image_generator_tool")
def image_generator_tool(prompt: str):
    """Generates an image using the Vertex AI Imagen model."""
    generation_model = ImageGenerationModel.from_pretrained(MODEL_IMAGEN)

    images = generation_model.generate_images(
        prompt=prompt,
        number_of_images=1,
        aspect_ratio="1:1",
        negative_prompt="",
        person_generation="allow_all",
        safety_filter_level="block_few",
        add_watermark=True,
        output_gcs_uri=GCS_IMAGE_BUCKET,
    )

    return {
        "status": "success",
        "message": f"Image generated {images[0]._gcs_uri}.",
    }


class ImageGeneratorAgent:
    SUPPORTED_CONTENT_TYPES = ["text/plain", "text"]
    SUPPORTED_CONTENT_TYPES_OUTPUT = ["text/plain", "image/png"]

    def invoke(self, query, sessionId) -> str:
        model = LLM(
            model=MODEL_GEMINI_CREW,  # Use base model name without provider prefix
        )

        prompt_enhancement = Agent(
            role="Prompt Enginner",
            goal=(
                "Help the user to create prompt in order to generate beautiful images for the story {query}"
            ),
            backstory=(
                "You are an expert in creating imagen4 prompts for image generation"
            ),
            verbose=False,
            allow_delegation=True,
            llm=model,
        )

        image_agent = Agent(
            role="Generate image for story",
            goal=("Help the narator to create images to illustrate story"),
            backstory=("You are an expert and helpful image creator."),
            verbose=False,
            allow_delegation=True,
            tools=[image_generator_tool],
            llm=model,
        )

        create_prompt_task = Task(
            description=PROMPT_ENHANCEMENT_TEMPLATE,
            agent=prompt_enhancement,
            expected_output="Return the prompt optimised",
        )

        generate_image_task = Task(
            description=IMAGE_GENERATOR_PROMPT,
            agent=image_agent,
            expected_output="Return the image asked by the user",
            context=[create_prompt_task],
        )

        crew = Crew(
            tasks=[create_prompt_task, generate_image_task],
            agents=[image_agent, prompt_enhancement],
            verbose=True,
            process=Process.sequential,
        )

        inputs = {"query": query, "session_id": sessionId}
        response = crew.kickoff(inputs)
        return response.raw


if __name__ == "__main__":
    agent = ImageGeneratorAgent()
    result = agent.invoke("A Super heros with a keyboard", sessionId="test_agent")
    logger.info(result)
