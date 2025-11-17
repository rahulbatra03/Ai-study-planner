from flask import Flask, render_template, request, send_file
from io import BytesIO
from datetime import datetime
from agents.planner_agent import PlannerAgent
from agents.schedule_agent import ScheduleAgent
from agents.research_agent import ResearchAgent
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

app = Flask(__name__)

# PDF Helper
def create_pdf_bytes(title: str, study_plan_text: str, topics_resources_text: str) -> bytes:
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    width, height = A4
    x_margin = 40
    y = height - 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_margin, y, title)
    y -= 30
    c.setFont("Helvetica", 10)

    for line in (study_plan_text + "\n\n" + topics_resources_text).splitlines():
        if y < 60:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 10)
        c.drawString(x_margin, y, line[:120])
        y -= 12

    c.save()
    buf.seek(0)
    return buf.read()


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    subjects_raw = request.form.get("subjects", "")
    days = int(request.form.get("days", "7"))
    hours = float(request.form.get("hours", "2"))

    subjects = [s.strip() for s in subjects_raw.split(",") if s.strip()]

    planner = PlannerAgent()
    scheduler = ScheduleAgent()
    researcher = ResearchAgent()

    base_plan = planner.create_study_plan(", ".join(subjects), days, hours)
    improved = scheduler.improve_schedule(base_plan)
    topics_resources = researcher.get_topics_and_resources(", ".join(subjects))

    return render_template("result.html",
                           subjects=", ".join(subjects),
                           days=days,
                           hours=hours,
                           plan_text=improved,
                           topics_text=topics_resources)


@app.route("/download_pdf", methods=["POST"])
def download_pdf():
    title = request.form.get("title", "Study Plan")
    plan_text = request.form.get("plan_text", "")
    topics_text = request.form.get("topics_text", "")
    pdf_bytes = create_pdf_bytes(title, plan_text, topics_text)
    return send_file(BytesIO(pdf_bytes), as_attachment=True, download_name="study_plan.pdf", mimetype="application/pdf")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
