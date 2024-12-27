import sqlite3


def convert(value):
    if value.startswith("~"):
        return value.strip("~")
    if not value:
        value = "0"
    return float(value)


conn = sqlite3.connect("food.db")
cur = conn.cursor()

cur.execute(
    """
            create table food(
            id text primary key,
            desc text,
            water float,
            kcal float,
            protein float,
            fat float,
            ash float,
            carbs float,
            fiber float,
            sugar float
            )
            """
)
query = "insert into food values(?,?,?,?,?,?,?,?,?,?)"
fields_count = 10
for line in open("ABBREV.txt"):
    fields = line.split("^")
    vals = [convert(f) for f in fields[:fields_count]]
    cur.execute(query, vals)

conn.commit()
conn.close()
