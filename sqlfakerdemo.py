from sqlfaker.database import Database

my_db = Database(db_name="campusdb")
# add columns to studyprogram
my_db.add_table("studentprogram", 20)
my_db.add_table("student", 100)

my_db.tables["studyprogram"].add_primary_key(column_name="studyprogram_id")
my_db.tables["studyprogram"].add_column(
    column_name="shortname", data_type="varchar(50)", data_target="name"
)
my_db.tables["studyprogram"].add_column(
    column_name="startdate", data_type="date", data_target="date"
)
# add columns to student
my_db.tables["student"].add_primary_key(column_name="student_id")
my_db.tables["student"].add_column(
    column_name="firstname", data_type="varchar(50)", data_target="first_name"
)
my_db.tables["student"].add_column(
    column_name="lastname", data_type="varchar(50)", data_target="last_name"
)
my_db.tables["student"].add_foreign_key(
    column_name="studiengang_id",
    target_table="studiengang",
    target_column="studiengang_id",
)
my_db.generate_data()
my_db.export_sql("test.sql")
