import os

from crewai import Agent
from crewai import Task
from langchain_groq import ChatGroq


class SoftwareDeveloper:
  description = "I'am specialized in the implementation of Java Source Code. I'am a specilist in Jakarta Enterprise and the Application Server Quarkus."
  model = "mixtral-8x7b-32768"
  goal = f"Create a object orientated source code solution base on the domain model and technology which has been created by the software architect."
  role = "Software Developer"
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
        max_rpm=29)

  def createTaskCreateSourceCode(self):
    return Task(
        description=f"Create a source code files based on output of the domain model task of the software architect",
        agent=self.agend,
        expected_output=f"A source code implementation files by on the architecture which was designed by the software architect",
        human_input=False,
        output_file="./output/sourcecode*.java"
    )
