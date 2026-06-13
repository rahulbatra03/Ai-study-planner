from agents.llm_client import get_llm

class PlannerAgent:
    def __init__(self):
        self.model = get_llm()

    def create_study_plan(self, subjects, days, hours_per_day):
        prompt = f"""
        You are an AI Study Planner expert. Create a CONCISE {days}-day study plan.
        Subjects: {subjects}
        Daily limit: {hours_per_day} hours

        RULES:
        - Keep each day SHORT and focused (max 150 words per day)
        - Format: Day X: Topic | Time allocation | Key focus
        - No long explanations, just actionable tasks
        - Keep it professional and clear

        Output exactly in this format:
        📅 Day 1: [Topic] | [Time] | [Focus area]
        📅 Day 2: [Topic] | [Time] | [Focus area]
        ... and so on
        """
        response = self.model.generate_content(prompt)
        return response.text
