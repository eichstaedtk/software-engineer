import os

from crewai import Crew

from domain.agents.RequirementEngineer import RequirementEngineer

os.environ[
  "GROQ_API_KEY"] = "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"
proxy = 'http://proxy.spk-berlin.de:3128'

os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy


class OneAgentOneTaskCrew:
  def __init__(self):
    self.re = RequirementEngineer("llama3-8b-8192")

  def run(self):
    crew = Crew(
        agents=[self.re.agend],
        tasks=[self.re.createTaskCreateUseCases()],
        verbose=True,
        max_rpm=5000,
        language="german"
    )

    return crew.kickoff()


if __name__ == "__main__":
  print("Welcome to the Software Engineering OneAgendOneTeam")
  print("------------------------------------------------")

  automation_crew = OneAgentOneTaskCrew()
  sdlc_result = automation_crew.run()

  print("\n\n########################")
  print("## Here are the results of your project:")
  print("########################\n")
  print(sdlc_result)
