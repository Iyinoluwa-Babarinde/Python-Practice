import sqlite3

try:
    #Establish database connection
    connection = sqlite3.connect("contacts.db")

    #Create cursor
    cursor = connection.cursor()

    #Function to create contacts table 
    def create_table():
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
        """)
        connection.commit()
        print(" Enter Contacts (Type 'done' as name to finish) ")

    #Function to insert name and contact
    def insert_name():
    # Use a loop to input contact names and phone numbers until 'done' is entered
        while True:
            name = input("Enter contact name (or 'done' to exit): ").strip()
            if name.lower() == 'done':
                break

            phone = input("Enter phone number: ").strip()

            cursor.execute("""
            INSERT INTO contacts (name, phone)
            VALUES (?, ?)
            """, (name, phone))

            connection.commit()
        print("Contacts added successfully!\n")

    #Function to display all contacts using a loop
    def display_contacts():
        print("\nAll Stored Contacts")
        cursor.execute("SELECT * FROM contacts")
        records = cursor.fetchall()
        if not records:
            print("No contacts found.")
        else:
            for record in records:
                print(record)


    create_table()
    insert_name()
    display_contacts()

except sqlite3.Error as error:
    if "connection" in locals():
        connection.rollback()
    print("Database error occurred", error)

# Close the database connection
finally:
    if "connection" in locals():
        connection.close()
    print("\nApplication closed")