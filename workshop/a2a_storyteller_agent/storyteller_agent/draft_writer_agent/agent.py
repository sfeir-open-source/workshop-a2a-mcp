from google.adk import Agent
from constants import STATE_CURRENT_DOC, MODEL_GEMINI

draft_writer_agent = Agent(
    name="DraftWriterAgent",
    model=MODEL_GEMINI,
    description="""
    A creative writing assistant that generates the initial draft of a story based on the 
    provided search results, focusing on creating an engaging start.
    """,
    include_contents='none',
    instruction=f"""
    You are a Creative Writing Assistant. Your task is to write the first draft of a short 
    story (4-8 sentences) based on the provided content.

    **Content to use:**
    ```
    {{search_results}}
    ```

    **Your Goal:** Create an engaging and imaginative opening for a story. Introduce a character, 
    a vivid setting, or a compelling action to capture the reader's attention.

    **Instructions:**

    1.  **Use only the provided content** to write the story.
    2.  **Output only the story text.** Do not include any introductions or explanations.
    """,
    output_key=STATE_CURRENT_DOC
)
