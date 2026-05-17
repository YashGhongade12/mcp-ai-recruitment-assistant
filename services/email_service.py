import smtplib
from email.mime.text import MIMEText


def send_email(candidate_email, candidate_name, status, score):

    sender_email = "yashghongade1273@gmail.com"
    app_password = "scsr gnyo nyxy etba"

    if status == "Shortlisted":
        subject = "Congratulations! You Have Been Shortlisted"

        body = f"""
Hello {candidate_name},

Congratulations!

We are pleased to inform you that you have been shortlisted for the next stage of our recruitment process.

Your screening score: {score}/100

Our HR team will contact you soon.

Best regards,
AI Recruitment Team
        """

    else:
        subject = "Application Update"

        body = f"""
Hello {candidate_name},

Thank you for applying.

After reviewing your profile, we are moving forward with other candidates whose experience more closely matches our current requirements.

We appreciate your interest.

Best regards,
AI Recruitment Team
        """

    msg = MIMEText(body)
    
    msg["Subject"] = subject
    msg["From"] = f"AI Recruitment Team <{sender_email}>" # Now perfect email will visible on mail
    msg["To"] = candidate_email

    server = smtplib.SMTP("smtp.gmail.com", 587) # Port no for SMTP mail
    server.starttls()
    server.login(
        sender_email,
        app_password,
        )
    server.sendmail(msg["From"], candidate_email, msg.as_string())
    server.quit()