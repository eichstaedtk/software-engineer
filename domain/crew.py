import os

from crewai import Crew

from groqagent import CustomAgents
from tasks import CustomTasks

# Set up environment variables
os.environ[
  "GROQ_API_KEY"] = "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"


class BusinessAutomationCrew:
  def __init__(self, business_type):
    self.business_type = business_type
    self.agents = CustomAgents()
    self.tasks = CustomTasks()

  def run(self):
    agents = {
      "requirement_engineer": self.agents.create_agent("Requirements Engineer"),
      "software_architect": self.agents.create_agent("Software Architect"),
      "software_developer": self.agents.create_agent("Software Developer")
    }

    tasks = {
      "use_case_creation": self.tasks.create_task(
          agents["requirement_engineer"],
          self.business_type,
          "use_case_creation"),
      "create_architecture_design": self.tasks.create_task(
          agents["software_architect"],
          self.business_type,
          "create_architecture_design"),
      "create_source_code": self.tasks.create_task(
          agents["software_developer"],
          self.business_type,
          "create_source_code")
    }

    crew = Crew(
        agents=list(agents.values()),
        tasks=list(tasks.values()),
        verbose=False
    )

    return crew.kickoff()


if __name__ == "__main__":
  print("Welcome to the Software Engineering Team Setup")
  print("------------------------------------------------")
  business_type = input(
      "Which Requirements are relevant for your software project?").strip()

  automation_crew = BusinessAutomationCrew(business_type)
  business_plan = automation_crew.run()

  print("\n\n########################")
  print("## Here are the results of your business automation project:")
  print("########################\n")
  print(business_plan)
