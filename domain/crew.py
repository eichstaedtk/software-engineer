import os

from crewai import Crew

from domain.agents.RequirementEngineer import RequirementEngineer
from domain.agents.SoftwareArchitect import SoftwareArchitect
from domain.agents.SoftwareDeveloper import SoftwareDeveloper

# Set up environment variables
os.environ[
  "GROQ_API_KEY"] = "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"


class SoftwareEngineeringCrew:
  def __init__(self):
    self.re = RequirementEngineer()
    self.sa = SoftwareArchitect()
    self.sd = SoftwareDeveloper()

  def run(self):
    agents = {
      "requirement_engineer": self.re.agend,
      "software_architect": self.sa.agend,
      "software_developer": self.sd.agend
    }

    tasks = {
      "use_case_creation": self.re.createTaskCreateUseCases(),
      "create_architecture_design": self.sa.createTaskCreateDomainModel(),
      "create_source_code": self.sd.createTaskCreateSourceCode()
    }

    crew = Crew(
        agents=list(agents.values()),
        tasks=list(tasks.values()),
        verbose=True,
        max_rpm=5000,
        language="german"
    )

    return crew.kickoff()


if __name__ == "__main__":
  print("Welcome to the Software Engineering Team Setup")
  print("------------------------------------------------")

  automation_crew = SoftwareEngineeringCrew()
  sdlc_result = automation_crew.run()

  print("\n\n########################")
  print("## Here are the results of your project:")
  print("########################\n")
  print(sdlc_result)
