import sqlite3

conn = sqlite3.connect("students.db", check_same_thread=False)
cursor = conn.cursor()

# CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

conn.commit()

# SEED DATA (5 students)
cursor.execute("SELECT COUNT(*) FROM students")
count = cursor.fetchone()[0]

if count == 0:
    students = [
        ("Pratham", 21, "CS"),
        ("Alex", 20, "IT"),
        ("Sarah", 22, "AI"),
        ("John", 23, "Math"),
        ("Maya", 21, "Physics")
    ]

    cursor.executemany(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        students
    )
    conn.commit()



def get_all_students():                      # Read all the data on table
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    return [
        {"id": r[0], "name": r[1], "age": r[2], "course": r[3]}
        for r in rows
    ]


def get_student(student_id):                                # Read one data
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    row = cursor.fetchone()

    if row:
        return {"id": row[0], "name": row[1], "age": row[2], "course": row[3]}
    return None



def add_student(student):                         # Creating data
    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (student["name"], student["age"], student["course"])
    )
    conn.commit()

    return {"message": "Student added"}



def delete_student(student_id):                 # Removing data
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

    return {"message": "Student deleted"}