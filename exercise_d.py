import sqlite3

try:
    #Establish database connection
    connection = sqlite3.connect("contacts.db")

    #Create cursor
    cursor = connection.cursor()

    # Function to create a table contacts if it doesn't already exist[cite: 26, 44, 46]
    def create_table():
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
        """)
        connection.commit()
        print("Enter Three Contacts")

    # Function to insert contacts
    def insert_contacts():
        for i in range(1, 4):
            print(f"\nContact {i}:")
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
        # Insert each contact into the table using parameterised queries[cite: 27, 35, 36, 44, 46]
        cursor.execute("""
            INSERT INTO contacts (name, phone)
            VALUES (?, ?)
            """, (name, phone))
        connection.commit()

    create_table() 
    insert_contacts()
   
except sqlite3.Error as error:
    if "connection" in locals():
        connection.rollback()
    print("Database error occurred", error)

# Close the database connection
finally:
    if "connection" in locals():
        connection.close()
    print("\nApplication closed")