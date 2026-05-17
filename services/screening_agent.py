from mcp_servers.resume_server import ResumeMCPServer
from mcp_servers.jd_server import JDMatcherMCPServer
from mcp_servers.email_server import EmailMCPServer
from mcp_servers.db_server import DatabaseMCPServer


class ScreeningAgent:

    def __init__(self):
        self.resume_server = ResumeMCPServer()
        self.jd_server = JDMatcherMCPServer()
        self.email_server = EmailMCPServer()
        self.db_server = DatabaseMCPServer()

    def process_candidate(
        self,
        mysql,
        full_name,
        email,
        phone,
        skills,
        resume_path
    ):

        extracted_text = self.resume_server.read_resume(resume_path)

        score, matched_skills = self.jd_server.evaluate_candidate(extracted_text)

        if score >= 60:
            status = "Shortlisted"
        else:
            status = "Rejected"

        self.email_server.notify_candidate(
            email,
            full_name,
            status,
            score
        )

        self.db_server.save_candidate(
            mysql,
            full_name,
            email,
            phone,
            skills,
            resume_path,
            extracted_text,
            score,
            status
        )

        return status, score, matched_skills