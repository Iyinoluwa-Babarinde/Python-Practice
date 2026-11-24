import sqlite3
connection = sqlite3.connect('database.db')
print("Database connection succesful.")
cursor = connection.cursor()


def create_contact():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contact(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone INTEGER
    )
    """)

    connection.commit()

    print("Student table successfully created")


def insert_contact():
    for i in range (3):
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        phone = input("Enter phone number: ")

    
        cursor.execute("""
            INSERT INTO contact ( id, name, phone)
            VALUES (?,?,?)
            """, (id, name, phone))
    
    connection.commit()
    print("Contact record updated")


    connection.commit()


create_contact()
insert_contact()
connection.close()