from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://postgres:12345@localhost/postgres"
db = create_engine(db_connection_string)

insert_sql = text("""
                  INSERT INTO subject (subject_id, subject_title)
                  VALUES (:new_id, :new_title)
                  """)
select_sql = text("SELECT * FROM subject WHERE subject_id = :new_id")
delete_sql = text("DELETE FROM subject WHERE subject_id = :new_id")
update_sql = text("""
                  UPDATE subject SET subject_title= :update_title
                  WHERE subject_id= :new_id
                  """)
count_sql = text("SELECT COUNT(*) FROM subject")


# Проверка соединения
def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[2] == "subject"


# Добавление предмета
def test_insert_new_subject():
    connection = db.connect()
    transaction = connection.begin()

    # Создание нового предмета
    connection.execute(insert_sql, {"new_id": 17, "new_title": "Statistics"})
    row = connection.execute(select_sql, {"new_id": 17}).fetchone()
    assert row[1] == "Statistics"

    # Удаление созданного предмета
    connection.execute(delete_sql, {"new_id": 17})

    transaction.commit()
    connection.close()


# Изменение предмета
def test_update_new_subject():
    connection = db.connect()
    transaction = connection.begin()

    # Создание нового предмета
    connection.execute(insert_sql, {"new_id": 17, "new_title": "Statistics"})
    row = connection.execute(select_sql, {"new_id": 17}).fetchone()
    assert row[1] == "Statistics"

    # Изменение созданного предмета
    connection.execute(update_sql, {"new_id": 17, "update_title": "Music"})
    row = connection.execute(select_sql, {"new_id": 17}).fetchone()
    assert row[1] == "Music"

    # Удаление созданного предмета
    connection.execute(delete_sql, {"new_id": 17})

    transaction.commit()
    connection.close()


def test_delete_new_subject():
    connection = db.connect()
    transaction = connection.begin()

    # Подсчет строк до изменения
    initial_count = connection.execute(count_sql).scalar()

    # Создание нового предмета
    connection.execute(insert_sql, {"new_id": 17, "new_title": "Statistics"})
    row = connection.execute(select_sql, {"new_id": 17}).fetchone()
    assert row[1] == "Statistics"

    # Удаление созданного предмета
    connection.execute(delete_sql, {"new_id": 17})

    # Подсчет после изменений
    final_count = connection.execute(count_sql).scalar()
    assert initial_count == final_count

    transaction.commit()
    connection.close()
