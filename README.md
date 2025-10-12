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

### Google Cloud Setup ☁️

First, you need to set up Google Cloud CLI and authentication:

1. **Install Google Cloud CLI**:
   Follow the instructions from: https://cloud.google.com/sdk/docs/install-sdk

2. **Authenticate with Google Cloud**:
   ```bash
   gcloud auth login
   gcloud auth application-default login
   ```

3. **Set your project**:
   ```bash
   gcloud config set project <PROJECT_ID>
   ```

### Configuration Setup 🔧

Before starting, you need to configure a couple of variables in `config.py`:

1. **Google Cloud Storage bucket for images** 🗄️ - Update `GCS_IMAGE_BUCKET` with your workshop bucket
2. **Toolbox endpoint** 🔧 - Update `TOOLBOX_ENDPOINT` with the Cloud Run URL from the `par-devfest-sfeir` Google Cloud Project

### Environment Variables 🔐

At the root of every agent directory, you need to create a `.env` file with the following environment variables:

```bash
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=<PROJECT_ID>
GOOGLE_CLOUD_LOCATION=us-central1
```

## Installation 📦

First, create and activate a virtual environment:

```bash
python3.11 -m venv .venv
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

## Usage 🚀

### To start image generator A2A server
From the solution (or workshop) folder:
```bash
uv run a2a_image_generator_agent/
```

### To start storyteller A2A server
From the solution (or workshop) folder:
```bash
uv run a2a_storyteller_agent/
```

### Start web UI
From the solution (or workshop) folder:
```bash
adk web
```

## Workshop TODOs 📝

### Storyteller Agent
ADK documentation: https://google.github.io/adk-docs/agents/workflow-agents.
- **Draft Writer Agent**: `workshop/a2a_storyteller_agent/storyteller_agent/draft_writer_agent/agent.py`
  - Implement the DraftWriterAgent that generates the initial draft of a story (4-8 sentences) based on search results.
- **Refinement Loop**: `workshop/a2a_storyteller_agent/storyteller_agent/refinement_loop/agent.py`
  - Add critic_agent and editor_agent to the sub_agents list in the LoopAgent configuration.
  - It might also be a good idea to limit the number of iterations 😉 

In order to test this part of the workshop, start adk web from `workshop/a2a_storyteller_agent/` folder.

Now let's add an A2A wrapper!

### A2A Wrapper
- **Agent Skill & Card**: `workshop/a2a_storyteller_agent/__main__.py`
  - Create AgentSkill for story creation with id, name, description, tags, and examples.
  - Create AgentCard for storyteller agent with name, description, url, version, input/output modes, capabilities, and skills.
  
  Need help? Get inspired by a2a_image_generator_agent implementation.

  Curious how to test it? The `a2a-inspector` from the debugging section can come in handy!

### Configuration
- **A2A Server URLs**: `workshop/config.py`
  - Add the URLs for the A2A servers (A2A_IMAGE_GENERATION_URL and A2A_STORYTELLER_URL).

## Debugging 🔍

### Testing Individual Agents

To test and debug individual agents, you can use the **[a2a-inspector](https://github.com/a2aproject/a2a-inspector)** tool, which provides a user-friendly interface for interacting with your agents.

#### Installation
```bash
# Clone the a2a-inspector repository
git clone https://github.com/a2aproject/a2a-inspector.git
cd a2a-inspector

# Follow the installation instructions in the repository
```

#### Usage
1. **Start your agent server** (e.g., `uv run a2a_image_generator_agent/`)
2. **Launch a2a-inspector** and connect to your agent's endpoint
3. **Send test messages** to verify agent behavior and responses
4. **Monitor logs** to troubleshoot any issues
