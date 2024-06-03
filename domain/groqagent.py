import os

from crewai import Agent
from langchain_groq import ChatGroq


class CustomAgents:
  def __init__(self):
    self.llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="mixtral-8x7b-32768",
    )

  def create_agent(self, role):
    descriptions = {
      "Requirements Engineer": "I'am specialized in manage all software product requirements. My job is it to collect, write and prioritize all requirements of all stakeholder.",
      "Software Architect": "I'am specialized in design software solutions, select proper technologie and risk management. I'am a expert in Domain Driven Design and Use Case Driven Software Engineering.",
      "Software Developer": "I'am specialized in the implementation of Java Source Code. I'am a specilist in Jakarta Enterprise and the Application Server Quarkus."
    }

    goals = {
      "Requirements Engineer": f"Identify,collect, prioritize and manage all requirements of all stakeholder.",
      "Software Architect": f"Design the best solution based an all requirements. Therefore the co working with the requirements engineer is very important.",
      "Software Developer": f"Create a smart and maintable source code solution base on the architecture and technology which has been developed by the software architect."
    }

    return Agent(
        role=role,
        backstory=descriptions[role],
        goal=goals[role],
        verbose=True,
        llm=self.llm,
        max_rpm=29,
    )
