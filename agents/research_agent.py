from agents.llm_client import get_llm

class ResearchAgent:
    def __init__(self):
        self.model = get_llm()

    def get_topics_and_resources(self, subjects):
        prompt = f"""
        You are an expert Academic Research AI. Create a CONCISE resource list.

        Subjects: {subjects}

        RULES:
        - List ONLY 5-7 most important topics per subject
        - Suggest ONLY top 3-4 resources (not 10+)
        - Keep descriptions SHORT (1 line max)
        - YouTube channels in a SEPARATE highlighted section
        - Be specific: include channel/course names

        Output in EXACTLY this format:

        📚 SUBJECT: [Subject Name]

        🎯 Key Topics:
        • [Topic 1]
        • [Topic 2]
        • [Topic 3]
        (max 7 topics)

        📖 Best Resources:
        • [Website/Platform]: [Brief description]
        • [Website/Platform]: [Brief description]

        🎥 YOUTUBE CHANNELS (Highlighted):
        ▶ [Channel Name]: [One line description]
        ▶ [Channel Name]: [One line description]

        Keep entire output under 300 words per subject.
        """
        response = self.model.generate_content(prompt)
        return response.text
