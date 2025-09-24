from google.adk.agents import LlmAgent
from constants import STATE_CURRENT_DOC, COMPLETION_PHRASE, MODEL_GEMINI
from .tools import exit_loop

editor_agent = LlmAgent(
    name="EditorAgent",
    description="""
    An editor agent that refines the story draft based on the critic's feedback. It applies the 
    suggested changes to improve the document or exits the refinement loop if the story is deemed complete.
    """,
    model=MODEL_GEMINI,
    include_contents='none',
    instruction=f"""
    You are a Creative Writing Assistant. Your task is to refine a document based on 
    the provided critique or to exit the process if the story is complete.

    **Current Document:**
    ```
    {{current_document}}
    ```
    
    **Critique/Suggestions:**
    ```
    {{criticism}}
    ```
    
    **Instructions:**
    
    1.  **If the critique is "{COMPLETION_PHRASE}"**, you must call the `exit_loop` function and 
    output nothing else.
    2.  **If the critique contains feedback**, carefully apply the suggestions to improve the document 
    and output only the refined text.
    3.  **Do not add any explanations or introductions.**
    """,
    tools=[exit_loop],  # exit_loop tool
    output_key=STATE_CURRENT_DOC
)
