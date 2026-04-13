from sqlalchemy import create_engine, text


class Students:
    __scripts = {
        "insert": text("""
            INSERT INTO student(user_id, level, education_form, subject_id)
            VALUES (:user_id, :level, :education_form, :subject_id)
        """),
        "select by id": text("SELECT * FROM student WHERE user_id = :user_id"),
        "update": text("""
            UPDATE student
            SET level = :level, education_form = :education_form
            WHERE user_id = :user_id
        """),
        "delete by id": text("DELETE FROM student WHERE user_id = :user_id"),
        "max id": text("SELECT MAX(user_id) FROM student"),
        "exists": text("SELECT 1 FROM student WHERE user_id = :user_id")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def create_student(self, user_id, level, education_form, subject_id):
        self.db.execute(
            self.__scripts["insert"],
            user_id=user_id,
            level=level,
            education_form=education_form,
            subject_id=subject_id
        )

    def get_student_by_id(self, user_id):
        return self.db.execute(
            self.__scripts["select by id"],
            user_id=user_id
        ).fetchone()

    def update_student(self, user_id, level, education_form):
        self.db.execute(
            self.__scripts["update"],
            user_id=user_id,
            level=level,
            education_form=education_form
        )

    def delete_student(self, user_id):
        self.db.execute(self.__scripts["delete by id"], user_id=user_id)

    def get_max_user_id(self):
        result = self.db.execute(self.__scripts["max id"]).fetchone()
        return result[0] if result and result[0] else 10000

    def student_exists(self, user_id):
        result = self.db.execute(
            self.__scripts["exists"],
            user_id=user_id
        ).fetchone()
        return result is not None
