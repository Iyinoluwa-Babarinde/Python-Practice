import sqlite3
connection = sqlite3.connect('database.db')
print("Database connection succesful.")
cursor = connection.cursor()

students = [('101', 'John', 'Compuer Engineering', '300'),
        ('102', 'Mary', 'Computer Science', '300')]


def create_students():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT,
            level INTEGER
    )
    """);

    connection.commit()

    print("Student table successfully created")


def insert_students():
    cursor.executemany("""
        INSERT INTO students (student_id, name, department, level)
        VALUES (?,?,?,?)
        """, students)
    
    connection.commit()
    print("Student record updated")

def select_students():
    cursor.execute("""
    SELECT name
    FROM students
    """)

    connection.commit()


create_students()
insert_students()
select_students()
connection.close()