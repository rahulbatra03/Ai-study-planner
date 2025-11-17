from agents.planner_agent import PlannerAgent
from agents.schedule_agent import ScheduleAgent
from agents.research_agent import ResearchAgent

def main():
    print(" AI Study Planner Started...\n")

    subjects = input("Enter subjects (comma separated): ")
    days = int(input("Enter number of days: "))
    hours = int(input("Enter study hours per day: "))

    print("\n⏳ Generating your AI-powered study plan...\n")

    # Initialize agents
    planner = PlannerAgent()
    scheduler = ScheduleAgent()
    researcher = ResearchAgent()

    # Create base study plan
    study_plan = planner.create_study_plan(subjects, days, hours)

    # Improve and structure it
    improved_plan = scheduler.improve_schedule(study_plan)

    # Get topics and resources
    topics_resources = researcher.get_topics_and_resources(subjects)

    # Output results
    print("\n Your Structured Study Plan:\n")
    print(improved_plan)

    print("\n Important Topics & Study Resources:\n")
    print(topics_resources)


if __name__ == "__main__":
    main()
