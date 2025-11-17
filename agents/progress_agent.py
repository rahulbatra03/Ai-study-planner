from agents.llm_client import get_llm

class ProgressAgent:
    def __init__(self):
        self.model = get_llm()

    def motivate(self, completed_hours, target_hours):
        prompt = f"""
        You are a motivational study coach.

        A student has completed {completed_hours} study hours
        out of a target of {target_hours} hours.

        Give a short motivational message to keep them going!
        Make it encouraging and positive.
        """
        response = self.model.generate_content(prompt)
        return response.text
