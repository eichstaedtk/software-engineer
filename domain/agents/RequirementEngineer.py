import os

from crewai import Agent
from crewai import Task
from crewai_tools.tools.file_read_tool.file_read_tool import FileReadTool
from langchain_groq import ChatGroq


class RequirementEngineer:
  description = "I'am specialized in manage software product requirements. My job is it to collect, write and prioritize all requirements of all stakeholder and transfer these into a Backlog."
  model = "mixtral-8x7b-32768"
  goal = f"Identify,collect, prioritize and manage all requirements of all stakeholder."
  role = "Requirements Engineer"
  file_read_tool = FileReadTool(file_path='requirements.txt')
  agend = None

  def __init__(self):
    self.llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="mixtral-8x7b-32768")
    self.agend = self.createAgend()

  def createAgend(self):
    return Agent(
        role=self.role,
        backstory=self.description,
        goal=self.goal,
        verbose=True,
        llm=self.llm,
        tools=[self.file_read_tool],
        max_rpm=29)

  def createTaskCreateUseCases(self):
    return Task(
        description=f"Write use cases for the following requirements and focus on the INVEST criteria. Create for the use cases a plantuml use case diagram.",
        agent=self.agend,
        expected_output=f"A plantuml use case diagram file in UML 2.0 syntax. Use the Use Case Guide 2.0 of Ivar Jacobson to create the use cases in a structured form.",
        human_input=False,
        output_file="./output/use_cases.txt"
    )
