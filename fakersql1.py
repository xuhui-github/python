# coding: utf-8
from sqlfaker.database import Database

my_db = Database(db_name="mydb")
my_db.add_table(table_name="student", n_rows=1500)
my_db.tables["student"]
my_db.tables["student"].add_primary_key(column_name="student_id")
my_db.tables["student"].add_column(column_name="student_id")
my_db.tables["student"].add_column(
    column_name="firstname", data_type="varchar(50)", data_target="first_name"
)
my_db.tables["student"].add_column(
    column_name="lastname", data_type="varchar(50)", data_target="last_name"
)
my_db.generate_data()
my_db.export_sql("test-student.sql")
