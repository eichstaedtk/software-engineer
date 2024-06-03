import os

from crewai import Agent
from crewai_tools import FileReadTool

os.environ[
  "OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"  # serper.dev API key
os.environ[
  "OPENAI_API_KEY"] = "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"
os.environ[
  "OPENAI_MODEL_NAME"] = "Llama3-70b-8192"

# OR

# Initialize the tool with a specific file path, so the agent can only read the content of the specified file


# Creating a requirements engineer agent with memory and verbose mode
requirements_engineer = Agent(
    role='Requirements Engineer',
    goal='Collect, prioritize and manage all software requirements',
    verbose=True,
    memory=True,
    backstory=(
      "Driven by curiosity, you're at the forefront of"
      "innovation, eager to explore and share knowledge that could change"
      "the world."
    ),
    tools=[file_read_tool],
    allow_delegation=True
)
