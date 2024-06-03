import os

from crewai import Agent
from crewai import Task
from langchain_groq import ChatGroq


class SoftwareArchitect:
  description = "I'am specialized in design software solutions, select proper technologie and risk management. I'am a expert in Domain Driven Design and use case driven software engineering."
  model = "mixtral-8x7b-32768"
  goal = f"Design the best domain model based on the concept of domain driven design and object orientation. Therefore the co working with the requirements engineer is very important."
  role = "Software Architect"
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
        max_rpm=29)

  def createTaskCreateDomainModel(self):
    return Task(
        description=f"Describe a possible solution for the use cases which are described by the requirements engineer and focus quality criteria maintability and usability. Use always the concept of software engineering.",
        agent=self.agend,
        expected_output=f"A plantuml domain model file in UML 2.0 syntax based one the use case diagram which has been generated by the requirements engineer",
        human_input=False,
        output_file="./output/domainmodel.txt"
    )