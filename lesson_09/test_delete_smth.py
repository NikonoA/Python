from sqlalchemy import create_engine
from sqlalchemy.sql import text


db_connect = "postgresql://postgres:123@localhost:5432/HomeWork"
db = create_engine(db_connect)


def test_delete_teacher():

    sql = text(
        "INSERT INTO teacher (\"email\", \"group_id\") VALUES (:email, :group)"
        )
    with db.connect() as connection:
        result = connection.execute(
            sql, email="Caribonara_very_tasty@gmail.com", group=5555555
            )
    select_sql = text(
        "SELECT \"group_id\" FROM teacher WHERE \"email\" = :email"
        )
    with db.connect() as connection:
        result = connection.execute(
            select_sql, email="Caribonara_very_tasty@gmail.com"
            )
        row = result.fetchone()

    if row:
        new_teacher = row["group_id"]
        delete_sql = text(
            "DELETE FROM teacher WHERE \"group_id\" = :gr_id"
            )
        with db.connect() as connection:
            connection.execute(delete_sql, gr_id=new_teacher)
    else:
        print("No teacher found with the given email.")
