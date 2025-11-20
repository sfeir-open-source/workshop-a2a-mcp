# A2A / MCP Workshop 🤖✨

```
    ╔══════════════════════════════════════╗
    ║  ⚡                                 ⚡ ║
    ║    🤖 AI Agent Orchestration 🎭       ║
    ║  ⚡                               ⚡ ║
    ║    ┌─────────────┐  ┌─────────────┐  ║
    ║    │   Image     │  │   Story     │  ║
    ║    │ Generator   │  │  Teller     │  ║
    ║    │    🎨       │  │   📖         │  ║
    ║    └─────────────┘  └─────────────┘  ║
    ║           │                │         ║
    ║           └──────┬─────────┘         ║
    ║                  │                   ║
    ║            ┌─────────────┐           ║
    ║            │ Orchestrator│           ║
    ║            │    🎯       │           ║
    ║            └─────────────┘           ║
    ║  ⚡                                ⚡ ║
    ╚══════════════════════════════════════╝
```

## Prerequisites ⚙️

### Google Cloud Shell ☁️

To make the environment configuration as smooth as possible, we'll use Cloud Shell for this workshop.

Click "Activate Cloud Shell" at the top right. Authorize it to make API calls on launch if needed. Then, click "Open in new window" followed by "Open Editor". This 
will provide an interface eerily similar to VSCode.

### Configuration Setup 🔧

Before starting, you need to configure a couple of variables in `config.py`:

1. **Google Cloud Storage bucket for images** 🗄️ - Update `GCS_IMAGE_BUCKET` with your workshop bucket
2. **Toolbox endpoint** 🔧 - Update `TOOLBOX_ENDPOINT` with the Cloud Run URL from the `par-devfest-sfeir` Google Cloud Project

## Installation 📦

First, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

To activate it in future sessions:

```bash
source .venv/bin/activate
```

Ensure you have the required dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables 🔐

At the root of every agent directory, you need to create a `.env` file with the following environment variables:

```bash
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=<PROJECT_ID>
GOOGLE_CLOUD_LOCATION=us-central1
```

This will help your agent know who is paying for its work. The agents are pretty strict and might refuse to work without this information.
Don't worry! We'll indicate every time you need to create the file! 😮‍💨

## 0. What do we have here? 🤔

Welcome, brave adventurer! You have two paths before you:
- **solution**: Everything is already coded—you just need to update the `config.py` file and add `.env` files (as mentioned above) in `a2a_image_generator_agent`, `a2a_storyteller_agent`, and `orchestrator_agent`. You'll be done in NO TIME! (NO TIME = 15 minutes)
- **workshop**: The path for intrepid explorers! Some code will be missing, and it's up to you to complete it! HINTs will be provided if you feel completely lost in the woods...

## 1. Your First Quest: Building Agents! 🎯

Ready to dive into the world of agents? Let's build a multi-agent!

The `workshop` folder contains an additional `agents` folder to help you build your first storytelling agent.
This agent was built using ADK. If you're curious about any part, you can check the documentation: https://google.github.io/adk-docs/agents/workflow-agents.

- **Draft Writer Agent**: `workshop/a2a_storyteller_agent/storyteller_agent/draft_writer_agent/agent.py`
  - Your mission: Implement the DraftWriterAgent that generates the initial draft of a story (4-8 sentences) based on search results.
  
  <details>
  <summary>💡 HINT</summary>
    Use the same structure as other ADK workflow agents:

    ```python
    draft_writer_agent = Agent(
    name="DraftWriterAgent",
    model=MODEL_GEMINI,
    description="""
    A creative writing assistant that generates the initial draft of a story based on the 
    provided search results, focusing on creating an engaging start.
    """,
    include_contents='none',
    instruction=f"""
    !!! COMPLETE THE AGENT INSTRUCTIONS
    """,
    output_key=STATE_CURRENT_DOC
    )
    ```

    You can also check the `solution/a2a_storyteller_agent/storyteller_agent/draft_writer_agent/agent.py` file for a reference implementation.
  </details>

- **Refinement Loop**: `workshop/a2a_storyteller_agent/storyteller_agent/refinement_loop/agent.py`
  - Your mission: Add critic_agent and editor_agent to the sub_agents list in the LoopAgent configuration.
  - Pro tip: It might also be a good idea to limit the number of iterations 😉 

  <details>
  <summary>💡 HINT</summary>
    After the agent description, add the sub-agents and maximum iterations:

    ```python
    sub_agents=[
        critic_agent,
        editor_agent,
    ],
    max_iterations=5
    ```
  </details>

### How to test it? Start web UI 🧪

Don't forget to place the `.env` file at the root of the `storyteller_agent` folder.
From the `workshop/agents` folder:
```bash
adk web
```

Now let's add an A2A wrapper and unlock the next level!

## 2. Level Up: A2A Wrapper 🚀

- **Agent Skill & Card**: `workshop/a2a_storyteller_agent/__main__.py`
  - Your mission: Create AgentSkill for story creation with id, name, description, tags, and examples.
  <details>
  <summary>💡 HINT</summary>
    Add AgentSkill to Storyteller agent A2A wrapper:

    ```python
    skill = AgentSkill(
            id="create_story",
            name="Story Creation Tool",
            description="Helps with writing stories",
            tags=["story creation"],
            examples=["What's new in Generative AI?"],
        )
    ```
    
  </details>
  
  - Your mission: Create AgentCard for storyteller agent with name, description, url, version, input/output modes, capabilities, and skills.
  
  <details>
  <summary>💡 HINT</summary>
    Add AgentCard to Storyteller agent A2A wrapper:

    ```python
    agent_card = AgentCard(
            name="Storyteller Agent",
            description="Helps with writing stories",
            url=f"http://{host}:{port}",
            version="1.0.0",
            defaultInputModes=StorytellerAgent.SUPPORTED_CONTENT_TYPES,
            defaultOutputModes=StorytellerAgent.SUPPORTED_CONTENT_TYPES_OUTPUT,
            capabilities=capabilities,
            skills=[skill],
        )
    ```
  </details>
Don't forget to place the `.env` file at the root of the `a2a_storyteller_agent` folder.

### How to start storyteller A2A server 🎬
From the solution (or workshop) folder:
```bash
uv run a2a_storyteller_agent/
```

### How to test A2A server 🔍

To test and debug, you can use the **[a2a-inspector](https://github.com/a2aproject/a2a-inspector)** tool, which provides a user-friendly interface for interacting with your agents.

#### Installation
```bash
# Clone the a2a-inspector repository
git clone https://github.com/a2aproject/a2a-inspector.git
cd a2a-inspector

# Follow the installation instructions in the repository
```

#### Usage
1. **Start your agent server** (e.g., `uv run a2a_image_generator_agent/`)
2. **Launch a2a-inspector** and connect to your agent's endpoint (e.g., `http://127.0.0.1:10002`)
3. **Send test messages** to verify agent behavior and responses
4. **Monitor logs** to troubleshoot any issues

## 3. The Grand Finale: Let's Wrap Everything Together! 🎉

- **A2A Server URLs**: `workshop/config.py`
  For our A2A servers to be used, we need to specify where they can be found!
  - Your mission: Add the URLs for the A2A servers (A2A_IMAGE_GENERATION_URL and A2A_STORYTELLER_URL).
  <details>
  <summary>💡 HINT</summary>
    Check the URLs and ports used to start the servers!

    ```python
    A2A_IMAGE_GENERATION_URL = "http://127.0.0.1:10001"
    A2A_STORYTELLER_URL = "http://127.0.0.1:10002"
    ```
  </details>

- **MCP ToolBox Connector**: `workshop/orchestrator_agent/sub_agent/agent.py`
  - Your mission: Add the MCP Toolbox connector to save the story. If you need help, check the corresponding package: https://pypi.org/project/toolbox-core/ .
  <details>
  <summary>💡 HINT</summary>
    Use the ToolboxSyncClient to connect to the toolbox and load the save tool:

    ```python
    toolbox = ToolboxSyncClient(TOOLBOX_ENDPOINT)
    save_story = toolbox.load_tool("insert-story")
    ```
  </details>

Place the `.env` file at the root of the `a2a_image_generator_agent` folder and `orchestrator_agent` folder. And you're all set to go!

## 4. Usage 🚀

### To start image generator A2A server 🎨
From the solution (or workshop) folder:
```bash
uv run a2a_image_generator_agent/
```

### To start storyteller A2A server 📖
From the solution (or workshop) folder:
```bash
uv run a2a_storyteller_agent/
```

### Start web UI 🌐
From the solution (or workshop) folder:
```bash
adk web
```

You can now choose the `orchestrator_agent` and test your storytelling solution! Time to see your creation come to life! ✨
