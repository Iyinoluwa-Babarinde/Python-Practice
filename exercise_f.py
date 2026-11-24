import sqlite3

try:
    # Establish database connection
    connection = sqlite3.connect("school.db")

    # Create cursor
    cursor = connection.cursor()

    #  Function to create student table
    def create_table():
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student (
            StudentID INTEGER PRIMARY KEY,
            StudentName TEXT NOT NULL,
            Class TEXT NOT NULL,
            Score REAL NOT NULL
        )
        """)
    connection.commit()

    # Function to insert the given student records into the student table
    def insert_details():
        initial_students = [
        (101, "David James", "SS1", 78.0),
        (102, "Mary Johnson", "SS2", 85.0),
        (103, "Peter Okoro", "SS1", 67.0),
        (104, "Grace Bello", "SS3", 92.0),
        (105, "Esther Ade", "SS2", 74.0)
        ]
        cursor.executemany("""
            INSERT OR IGNORE INTO student (StudentID, StudentName, Class, Score)
            VALUES (?, ?, ?, ?)
            """, initial_students)
        connection.commit()
        print("All Student Records")

    #Function to retrieve  and display all student records
    def retrieve_record():
        cursor.execute("SELECT * FROM student")
        records= cursor.fetchall()
        if not records:
            print("No record found.")
        else:
            for record in records:
                print(record)

    def retrieve_ss2():
        print("\nStudents in SS2")
        cursor.execute("""
            SELECT * FROM student
            WHERE Class = 'SS2'
            """)
        records_ss2 = cursor.fetchall()
        if not records_ss2:
            print("Records not found")
        else:
            for record in records_ss2:
                print(record)

    def statistics():
        print("\nStatistics")
        cursor.execute("""
            SELECT COUNT(*), MAX(Score), AVG(Score) FROM student
            """)
        stats = cursor.fetchone()
        print(f"Total Number of Students: {stats[0]}")
        print(f"Highest Score: {stats[1]}")
        print(f"Average Score: {stats[2]:.2f}")

    # Function to update the score of Peter Okoro from 67 to 75
    def update_record():
        cursor.execute("""
        UPDATE student
        SET Score = 75.0
        WHERE StudentID = 103
        """)
        connection.commit()
        print("\n--- vi. Updated Peter Okoro's Score to 75 ---")
        cursor.execute("SELECT * FROM student WHERE StudentID = 103")
        print(cursor.fetchone())

    # Function to delete the record of the student whose StudentID is 105
    def delete_record():
        cursor.execute("""
            DELETE FROM student
            WHERE StudentID = 105
            """)
        connection.commit()
        print("\n Student with ID 105 (Esther Ade)")

        cursor.execute("SELECT * FROM student")
        record_all = cursor.fetchall()
        if not record_all:
            print("No record found")
        else:
            for record in record_all:
                print(record)


    create_table()
    insert_details()
    retrieve_record()
    retrieve_ss2()
    statistics()
    update_record()
    delete_record()

except sqlite3.Error as error:
    if "connection" in locals():
        connection.rollback()
    print("Database error occurred", error)

# Close the database connection
finally:
    if "connection" in locals():
        connection.rollback()
    print("\nSchool management system session closed successfully.")