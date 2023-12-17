from sqlfaker.database import Database

# add database
my_db = Database(db_name="campusdb")

# add tables
my_db.add_table(table_name="student", n_rows=500)
my_db.add_table(table_name="studyprogram", n_rows=15)
# add columns to studyprogram table
my_db.tables["studyprogram"].add_primary_key(column_name="studyprogram_id")
my_db.tables["studyprogram"].add_column(column_name="shortname", data_type="varchar(50)", data_target="name")
my_db.tables["studyprogram"].add_column(column_name="startdate", data_type="date", data_target="date")

# add columns to student table
my_db.tables["student"].add_primary_key(column_name="student_id")
my_db.tables["student"].add_column(column_name="firstname", data_type="varchar(50)", data_target="first_name")
my_db.tables["student"].add_column(column_name="lastname", data_type="varchar(50)", data_target="last_name")
#my_db.tables["student"].add_foreign_key(column_name="studentprogram_id", target_table="studentprogram", target_column="studentprogram_id")
#my_db.generate_data()
my_db.export_sql("test.sql")

