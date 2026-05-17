from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os
from config import Config
from services.pdf_parser import extract_text_from_pdf
from services.skill_matcher import match_skills
from services.email_service import send_email
from services.screening_agent import ScreeningAgent

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    full_name = request.form["full_name"]
    email = request.form["email"]
    phone = request.form["phone"]
    skills = request.form["skills"]

    resume = request.files["resume"]

    resume_path = os.path.join(app.config["UPLOAD_FOLDER"], resume.filename)
    resume.save(resume_path)

    agent = ScreeningAgent()

    status, score, matched_skills = agent.process_candidate(
        mysql,
        full_name,
        email,
        phone,
        skills,
        resume_path
    )

    return render_template(
        "success.html",
        name=full_name,
        status=status,
        score=score,
        matched_skills=matched_skills
    )


if __name__ == "__main__":
    app.run(debug=True)