import os

from crewai import Crew

from domain.agents.MetadataManager import MetadataManager

os.environ[
  "GROQ_API_KEY"] = "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"
proxy = 'http://proxy.spk-berlin.de:3128'


# os.environ['http_proxy'] = proxy
# os.environ['HTTP_PROXY'] = proxy
# os.environ['https_proxy'] = proxy
# os.environ['HTTPS_PROXY'] = proxy


class LibraryNamedEntityCrew:
  def __init__(self):
    self.mm = MetadataManager("llama3-8b-8192")

  def run(self):
    crew = Crew(
        agents=[self.mm.agend],
        tasks=[self.mm.createTaskForNamedEntityRecognition()],
        verbose=True,
        max_rpm=5000,
        language="german"
    )

    return crew.kickoff()


if __name__ == "__main__":
  print("Welcome to the Library Named Entity Team")
  print("------------------------------------------------")

  automation_crew = LibraryNamedEntityCrew()
  sdlc_result = automation_crew.run()

  print("\n\n########################")
  print("## Here are the results of your project:")
  print("########################\n")
  print(sdlc_result)
