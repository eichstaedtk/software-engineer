import os

from crewai import Agent
from crewai import Task
from crewai_tools.tools.file_read_tool.file_read_tool import FileReadTool
from langchain_groq import ChatGroq


class RequirementEngineer:
  description = "Ich bin spezialisiert darauf, einen product owner beim Management aller Anforderungen an eine Software zu unterstützen."
  goal = f"Identifizieren, sammeln und priorisieren aller Anforderungen an die zu entwickelnde Software."
  role = "Requirements Engineer"
  file_read_tool = FileReadTool(file_path='./../requirements.txt')
  agend = None

  def __init__(self, llm):
    self.llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model=llm)
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
        description=f"Schreibe use cases für die nachfolgenden Anforderungen mit dem Fokus auf die INVEST Kriterien. Erstelle ein use case diagramm mit plantuml",
        agent=self.agend,
        expected_output=f"Eine use case datei in welcher jeder use case eine nummer, einen titel, eine kurze Beschreibung und das happy path szenario enthält."
                        f"Jede Beschreibung eines Use Cases soll sich am Use Case Guide 2.0 von Ivar Jacobson orientieren.",
        allow_delegation=False,
        human_input=True,
        output_file="./../output/use_cases.txt"
    )
