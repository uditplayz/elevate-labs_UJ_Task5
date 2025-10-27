import psycopg2

conn = psycopg2.connect(
    host="pgsql17elevate.postgres.database.azure.com",
    port=5432,
    user="postgres",
    password="mysqlserver@1",
    database="intern_demo"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM students;")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()