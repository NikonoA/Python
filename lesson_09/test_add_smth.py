from sqlalchemy import create_engine
from sqlalchemy.sql import text


db_connect = "postgresql://postgres:123@localhost:5432/HomeWork"
db = create_engine(db_connect)


def test_insert_subject():

    sql = text(
        "INSERT INTO subject "
        "(\"subject_title\") "
        "VALUES (:new_sub) RETURNING (\"subject_title\")"
        )
    with db.connect() as connection:
        result = connection.execute(sql, new_sub="Dancing")
        row = result.fetchone()
        new_subject = row["subject_title"]
        delete_sql = text(
            "delete from subject where (\"subject_title\") = (:title)"
            )
        connection.execute(delete_sql, title=new_subject)
