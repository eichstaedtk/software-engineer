from crewai import Task


class CustomTasks:
  def __init__(self):
    pass

  def create_task(self, agent, business_type, task_type):
    task_descriptions = {
      "use_case_creation": (
        f"Write use cases for the following requirements {business_type}, and focus on the INVEST criteria. Create for the use cases a plantuml use case diagram."
      ),
      "create_architecture_design": (
        f"Describe a possible solution for the use cases which are described by the Requirements Engineer and focus quality criteria maintability and usability. Use always the concept of software engineering."
      ),
      "create_source_code": (
        f"Create a source code project based on the recommended technologie of the Software Architect"
      )
    }

    expected_outputs = {
      "use_case_creation": (
        f"Structured Use cases for all requirements {business_type}, including a plantuml use case diagram. Use the Use Case Guide of Ivar Jacobson to create the use case in a structured form."
      ),
      "create_architecture_design": (
        f"A possible technologie stack, a selected programming language should be used and he should describe the system structure for the following requirements {business_type}"
      ),
      "create_source_code": (
        f"A source code implementation"
      )
    }

    return Task(
        description=task_descriptions[task_type],
        agent=agent,
        expected_output=expected_outputs[task_type]
    )
