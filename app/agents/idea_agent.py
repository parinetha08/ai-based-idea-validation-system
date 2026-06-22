"""Idea validation agent using ADK + LLM pipeline."""

from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from app.backend.services.prompt_builder import build_prompt
from app.backend.services.ollama_client import generate_response


def validate_startup_idea(
    idea: str,
    provider: str = "ollama",
    api_key: str = "",
) -> str:
    """Validate idea using selected provider."""

    prompt = build_prompt(idea)

    return generate_response(
        prompt=prompt,
        provider=provider,
        api_key=api_key,
    )


validation_tool = FunctionTool(func=validate_startup_idea)

_idea_agent = Agent(
    name="IdeaValidator",
    description="AI Startup Idea Validation Agent",
    instruction="""
You are a startup idea evaluation expert.

When given an idea:
- Evaluate market demand
- Identify risks
- Suggest improvements
- Provide structured output
""",
    tools=[validation_tool],
)


def run_idea_agent(
    idea: str,
    provider: str = "ollama",
    api_key: str = "",
) -> str:
    """Main pipeline entry point used by API."""

    print("✅ ADK Agent is running")
    print(f"Idea received: {idea}")
    print(f"Provider selected: {provider}")

    response = validate_startup_idea(
        idea=idea,
        provider=provider,
        api_key=api_key,
    )

    print("✅ ADK Agent finished")

    return response
