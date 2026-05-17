from services.email_service import send_email


class EmailMCPServer:

    def notify_candidate(self, email, name, status, score):
        send_email(email, name, status, score)