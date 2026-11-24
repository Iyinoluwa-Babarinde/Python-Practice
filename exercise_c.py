import sqlite3
try:
    # Establish database connection
    connection = sqlite3.connect("university_records.db")

    # Create cursor
    cursor = connection.cursor()

    # Create the students table 
    def create_table():
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            year_of_birth INTEGER NOT NULL
            )
            """)
        connection.commit()
        

    # Define the student records to insert
    student_records = [
    (1, "Peter", "Lee", "plee@university.edu", 1992),
    (2, "Jonathan", "Edwards", "jedwards@university.edu", 1994),
    (3, "Marilyn", "Johnson", "mjohnson@university.edu", 1993),
    (6, "Joe", "Kim", "jkim@university.edu", 1992),
    (12, "Haley", "Martinez", "hmartinez@university.edu", 1993),
    (14, "John", "Mfume", "jmfume@university.edu", 1991),
    (15, "David", "Letty", "dletty@university.edu", 1995)
    ]

    def insert_record():
        # Insert records 
        cursor.executemany("""
            INSERT OR IGNORE INTO students (id, first_name, last_name, email, year_of_birth)
            VALUES (?, ?, ?, ?, ?)
            """, student_records)
        connection.commit()
        print("Student records inserted successfully.")

    def retrieve_records():
        # Retrieve and display records to verify insertion
        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()
        if not records:
            print("No student records found.") 
        else: 
            for row in records:  
                print(row)


    create_table()
    insert_record()
    retrieve_records()

except sqlite3.Error as error:
        if "connection" in locals():
            connection.rollback()
        print("Database error occurred", error)

    # Close the database connection
finally:
    if "connection" in locals():
        connection.close()
    print("\nApplication closed")
