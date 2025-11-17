from agents.llm_client import get_llm

class ScheduleAgent:
    def __init__(self):
        self.model = get_llm()

    def create_schedule(self, subjects, total_hours):
        prompt = f"""
        You are an AI Study Time Management Expert.

        The student wants to study these subjects: {subjects}
        Total available study hours for today: {total_hours}

        Divide the hours into a productive schedule.
        Make sure each subject gets time.
        Include short breaks if needed.

        Output format:

        📅 Study Schedule:
        - Subject 1: X minutes
        - Subject 2: X minutes
        ...
        """
        response = self.model.generate_content(prompt)
        return response.text

    def improve_schedule(self, study_plan):
        prompt = f"""
        You are an AI Study Schedule Improver.
        Improve the following study plan by making it more structured,
        clear, productive, and include time distribution + short breaks.

        Study Plan:
        {study_plan}

        Output format:
        📌 Improved Study Plan:
        Day X:
        - Task (time)
        - Task (time)
        """
        response = self.model.generate_content(prompt)
        return response.text
