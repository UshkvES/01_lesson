from Students import Students

# Строка подключения - ЗАМЕНИТЕ НА ВАШУ!
DB_CONNECTION = "postgresql://ваш_user:ваш_пароль@localhost:5432/QA"

db = Students(DB_CONNECTION)


def test_create_student():
    new_id = db.get_max_user_id() + 1

    db.create_student(new_id, "Pre-Intermediate", "personal", 1)

    db_student = db.get_student_by_id(new_id)
    assert db_student is not None
    assert db_student[1] == "Pre-Intermediate"
    assert db_student[2] == "personal"
    assert db_student[3] == 1

    db.delete_student(new_id)


def test_update_student():
    new_id = db.get_max_user_id() + 1
    db.create_student(new_id, "Beginner", "group", 2)

    db.update_student(new_id, "Upper-Intermediate", "personal")

    db_student = db.get_student_by_id(new_id)
    assert db_student[1] == "Upper-Intermediate"
    assert db_student[2] == "personal"
    assert db_student[3] == 2

    db.delete_student(new_id)


def test_delete_student():
    new_id = db.get_max_user_id() + 1
    db.create_student(new_id, "Elementary", "personal", 3)

    assert db.student_exists(new_id) is True

    db.delete_student(new_id)

    assert db.student_exists(new_id) is False
