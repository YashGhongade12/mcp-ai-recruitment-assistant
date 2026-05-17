from services.pdf_parser import extract_text_from_pdf


class ResumeMCPServer:

    def read_resume(self, resume_path):
        return extract_text_from_pdf(resume_path)