REQUIRED_SKILLS = {
    "python": 20,
    "sql": 20,
    "llm": 20,
    "rag": 20,
    "gen ai": 20
}


def match_skills(resume_text): # Skills only taken from resume only not from form.
    resume_text = resume_text.lower()

    score = 0
    matched_skills = []

    for skill, points in REQUIRED_SKILLS.items():
        if skill in resume_text:
            score += points
            matched_skills.append(skill)

    return score, matched_skills