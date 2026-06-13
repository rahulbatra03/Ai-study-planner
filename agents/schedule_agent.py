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
        Improve this study plan - make it CONCISE, clear, and actionable.

        Original Plan:
        {study_plan}

        RULES:
        - Keep summary brief (max 2 lines per day)
        - Add 10-min breaks between 50-min study blocks
        - Use clear time blocks: Study | Break | Study
        - Include 1-2 key productivity tips only
        - Total output should be readable in 2 minutes

        Format:
        ⏰ IMPROVED PLAN (Concise Version):

        Day X:
        [Time] | Study: [Topic] (focus: X)
        [Time] | Break
        [Time] | Study: [Topic] (focus: Y)

        💡 Tips: [1-2 bullet points max]
        """
        response = self.model.generate_content(prompt)
        return response.text
