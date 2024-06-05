import os

from crewai import Agent
from crewai import Task
from crewai_tools.tools.file_read_tool.file_read_tool import FileReadTool
from langchain_groq import ChatGroq


# Hugging Face Token
# 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

class MetadataManager:
  description = "Ich bin spezialisiert darauf bibliothekarische Metadaten zu erstellen und verarbeiten. Die Daten liegen zum großen Teil im XML Format vor. "
  goal = f"Manage all Metadaten für die Präsentation im Web oder für die Verwendung in Anwendungen."
  role = "Metadata Manager"
  file_read_tool = FileReadTool(file_path='./../text.txt')
  agend = None

  def createAgend(self):
    return Agent(
        role=self.role,
        backstory=self.description,
        goal=self.goal,
        verbose=True,
        llm=self.llm,
        tools=[self.file_read_tool],
        max_rpm=29)

  def __init__(self, llm):
    self.llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model=llm)
    self.agend = self.createAgend()

  def createTaskForNamedEntityRecognition(self):
    return Task(
        description=f"Erkenne Personen, Orte und Institutionen bzw. Körperschaften innerhalb eines beliebigen Textes.",
        agent=self.agend,
        expected_output=f"Eine Liste mit erkannten Entitäten. Jede Entität ist gekennzeichnet mit dem entsprechenden Typ. Es können lediglich folgende Typen identifiziert werden: Person,Place,CorporateBody.",
        allow_delegation=False,
        human_input=False,
        output_file="./../output/namedentities.txt",
        async_execution=False
    )
