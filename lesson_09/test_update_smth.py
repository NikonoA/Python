from sqlalchemy import create_engine
from sqlalchemy.sql import text


db_connect = "postgresql://postgres:123@localhost:5432/HomeWork"
db = create_engine(db_connect)


def test_create_and_update_student():

    sql = text(
        "INSERT INTO student "
        "(\"level\", \"education_form\", \"subject_id\") "
        "VALUES (:level, :form, :id)"
        )
    with db.connect() as connection:
        connection.execute(sql, level="Beginner", form="personal", id=16)
    upd = text(
        "UPDATE student SET subject_id = :new_id WHERE subject_id = :old_id"
        )
    with db.connect() as connection:
        connection.execute(upd, new_id=10, old_id=16)
    select_sql = text(
        "SELECT subject_id FROM student WHERE subject_id = :new_id"
                      )
    with db.connect() as connection:
        result = connection.execute(select_sql, new_id=10).fetchone()

    if result:
        new_student = result["subject_id"]
        delete_sql = text(
            "DELETE FROM student WHERE \"subject_id\" = :sub_id"
            )
        with db.connect() as connection:
            connection.execute(delete_sql, sub_id=new_student)
