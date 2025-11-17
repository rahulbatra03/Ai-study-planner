from agents.llm_client import get_llm

class PlannerAgent:
    def __init__(self):
        self.model = get_llm()

    def create_study_plan(self, subjects, days, hours_per_day):
        prompt = f"""
        You are an AI Study Planner expert.
        Create a {days}-day study plan for subjects: {subjects}.
        Daily study limit: {hours_per_day} hours.
        Output format:
        Day X:
        - Task 1
        - Task 2
        """
        response = self.model.generate_content(prompt)
        return response.text
