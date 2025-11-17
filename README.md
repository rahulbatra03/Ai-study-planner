AI Study Planner Agent
Personalized Study Plan Generator using Gemini AI, Flask & Python
 Project Overview

AI Study Planner Agent is an AI-powered web application that generates a personalized study plan based on subjects, study duration, and daily study hours. It uses Gemini AI to create optimized schedules and allows users to download the plan as a PDF for offline use.

This project was built as part of the Kaggle Agents Intensive – Capstone Project.
--------------------------------------------------------------------------------------------------------------------
 One-Line Description

An AI agent that creates personalized study plans and schedules using Gemini AI, helping students learn more efficiently.
-------------------------------------------------------------------------------------------------------------------
 Problem Statement

Students often struggle to create a balanced and effective study plan that fits their available time, exam deadlines, and multiple subjects. Manual planning is time-consuming, inconsistent, and doesn’t adapt to different learning speeds.
--------------------------------------------------------------------------------------------------------------------
Why Agents?

AI Agents can:

Process user inputs & constraints intelligently

Allocate topic durations according to importance

Recommend learning strategies & resources

Automate the planning workflow end-to-end

Using an agent removes guesswork and gives students a structured and optimized path to study smarter, not harder.
--------------------------------------------------------------------------------------------------------------------
Architecture Overview

User Input ➜ Flask Backend ➜ Gemini AI Study Planner Agent ➜ Study Plan Output (PDF)


Core Components

Component / File	              Purpose
app.py	                          Flask server, routing, PDF export
main.py	                          Orchestrates communication with the agent
agents/planner.py	              Core logic for generating study plan
agents/research.py	              Fetches additional learning guidance/resources
agents/progress.py	              Tracks time distribution & improvements
agents/llm_client.py	          Gemini AI API client wrapper
templates/index.html	          Frontend UI form
static/style.css	              Page styling

--------------------------------------------------------------------------------------------------------------------
Folder Structure

AI-Study-Planner/
│
├─ app.py
├─ main.py
├─ agents/
│   ├─ planner.py
│   ├─ research.py
│   ├─ progress.py
│   ├─ llm_client.py
│   └─ schedule.py
├─ templates/
│   └─ index.html
├─ static/
│   └─ style.css
├─ requirements.txt
└─ README.md
----------------------------------------------------------------------------------------------------------
Tech Stack
Area	          Technologies
Frontend	        HTML, CSS
Backend	            Python, Flask
AI Model	        Gemini AI API

Export PDF file download(Additional feature)
----------------------------------------------------------------------------------------------------------
Getting Started / How to Use

Follow these steps to run the AI Study Planner project on your system:


1️. Clone the Repository
git clone https://github.com/your-username/ai-study-planner.git
cd ai-study-planner

2️. Install Required Dependencies
Make sure you have Python 3.10+ installed, then run:

pip install -r requirements.txt

3. Create Environment Variables

Create a new .env file in the project root and add your Gemini API Key:

GEMINI_API_KEY=your_api_key_here
(Replace your_api_key_here with your actual Google Gemini API key.)

4.Run the Flask App

Start the application using:

python app.py
--------------------------------------------------------------------------------------------------------
WORKFLOW:

[ User Form ]
      ↓
[ Flask API (app.py) ]
      ↓
[ LLM Client → Gemini API ]
      ↓
 ┌─────────────────────────────┐
 |  Planner Agent              |
 |  Schedule Agent             |
 |  Progress Agent (optional)  |
 |  Research Agent (optional)  |
 └─────────────────────────────┘
      ↓
[ Final Study Plan Output ]
----------------------------------------------------------------------------------------------------------