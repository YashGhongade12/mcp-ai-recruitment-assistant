from services.skill_matcher import match_skills


class JDMatcherMCPServer:

    def evaluate_candidate(self, resume_text):
        return match_skills(resume_text)