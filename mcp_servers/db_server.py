class DatabaseMCPServer:

    def save_candidate(
        self,
        mysql,
        full_name,
        email,
        phone,
        skills,
        resume_path,
        extracted_text,
        score,
        status
    ):

        cursor = mysql.connection.cursor()

        query = """
            INSERT INTO candidates
            (
                full_name,
                email,
                phone,
                skills,
                resume_path,
                extracted_text,
                score,
                status
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            full_name,
            email,
            phone,
            skills,
            resume_path,
            extracted_text,
            score,
            status
        )

        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()