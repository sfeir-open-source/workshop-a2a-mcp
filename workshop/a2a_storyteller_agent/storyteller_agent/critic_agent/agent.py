from google.adk.agents import LlmAgent
from constants import STATE_CRITICISM, COMPLETION_PHRASE, MODEL_GEMINI

critic_agent = LlmAgent(
    name="CriticAgent",
    description="""
    An LLM agent that acts as a constructive critic, reviewing the story draft for clarity, engagement, 
    and coherence. It provides specific, actionable feedback or signals completion if the draft is satisfactory.
    """,
    model=MODEL_GEMINI,
    include_contents='none',
    instruction=f"""
    You are a Constructive Critic AI. Your task is to review the following document and 
    provide feedback.

    **Document to Review:**
    ```
    {{current_document}}
    ```

    **Your Goal:** Provide balanced and actionable feedback to improve the document's clarity, 
    engagement, and coherence.
    
    **Instructions:**
    
    1.  **If you find clear, actionable ways to improve the document**, provide your suggestions 
    concisely. Focus on 1-2 key improvements.
    2.  **If the document is already coherent and effective**, respond with the exact phrase: 
    "{COMPLETION_PHRASE}"
    3.  **Do not add any extra explanations or introductions.** Output only the critique or the completion phrase.
    """,
    output_key=STATE_CRITICISM
)
