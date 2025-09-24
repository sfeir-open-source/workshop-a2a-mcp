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
     ║           │    🎯       │            ║
    ║            └─────────────┘           ║
    ║  ⚡                                ⚡ ║
    ╚══════════════════════════════════════╝
```

## Prerequisites ⚙️

Before starting, you need to configure a couple of variables in `config.py`:

1. **Google Cloud Storage bucket for images** 🗄️ - Update `GCS_IMAGE_BUCKET` with your workshop bucket
2. **Toolbox endpoint** 🔧 - Update `TOOLBOX_ENDPOINT` with the Cloud Run URL from the `par-devfest-sfeir` Google Cloud Project

## Installation 📦

First, create and activate a virtual environment:

```bash
python -m venv .venv
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

### To start story teller A2A server
From the solution (or workshop) folder:
```bash
uv run a2a_storyteller_agent/
```

### Start web UI
From the solution (or workshop) folder:
```bash
adk web 
```

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
