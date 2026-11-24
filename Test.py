import sqlite3
connection = sqlite3.connect('student.db')
cursor = connection.cursor()

print("Sqlite3 connected")

def CREATE_TABLE():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Student(
            ID INTEGER PRIMARY KEY,
            First_name TEXT,
            LAST_name TEXT,
            Email VARCHAR,
            Year_of_Birth INTEGER)
        """)
        
    connection.commit()
    print("Table created")
    

def insert_student():
    student = ['(id = input("Enter ID:"))',
    '(first = input("Enter First Name: "))',
    '(last = input("Enter Last Name: "))',
    '(email = input("Enter Email: "))',
    '(year = input("Enter Year: "))'
    ]

    cursor.executemany("""
    INSERT INTO Student (ID, First_name, LAST_name, Email, Year_of_Birth)
    VALUES (?,?,?,?,?)
    """, student)
    
    connection.commit()
    print("Database updated")


CREATE_TABLE()
insert_student()
connection.close()