from agents.llm_client import get_llm

class ResearchAgent:
    def __init__(self):
        self.model = get_llm()

    def get_topics_and_resources(self, subjects):
        prompt = f"""
        You are an expert Academic Research AI.

        The student wants to study the following subjects:
        {subjects}

        For each subject:
        1. List the most important topics to study.
        2. Suggest useful learning resources such as:
           - YouTube channels
           - Free courses
           - Websites
           - Notes/PDF sources

        Output format:

         Subject Name:
        Topics:
        - Topic 1
        - Topic 2
        - Topic 3

        Resources:
        - Resource 1
        - Resource 2
        - Resource 3
        """
        response = self.model.generate_content(prompt)
        return response.text
