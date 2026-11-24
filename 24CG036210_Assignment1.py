import tkinter as tk
from tkinter import messagebox
from docx import Document


def submit_details(name_entry, matric_entry, dept_entry):
    name = name_entry.get().strip()
    matric = matric_entry.get().strip()
    department = dept_entry.get().strip()

    # Check that all fields are filled
    if not name or not matric or not department:
        messagebox.showwarning("Missing Information", "Please fill in all fields.")
        return

    details = (
        f"Name: {name}\n"
        f"Matric Number: {matric}\n"
        f"Department: {department}"
    )

    # Display details in a message box
    messagebox.showinfo("Student Details", details)

    # Save a copy in student_info.txt
    with open("student_info.txt", "a", encoding="utf-8") as txt_file:
        txt_file.write(details + "\n" + "-" * 30 + "\n")

    # Save another copy in student_info.docx
    try:
        doc = Document("student_info.docx")
    except Exception:
        doc = Document()
    doc.add_paragraph(details)
    doc.add_paragraph("-" * 30)
    doc.save("student_info.docx")

    # Clear the form
    name_entry.delete(0, tk.END)
    matric_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)

    # Confirm success
    messagebox.showinfo("Success", "Details saved to student_info.txt and student_info.docx!")


def main():
    root = tk.Tk()
    root.title("Student Information App")
    root.geometry("420x220")

    tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=8, sticky="w")
    tk.Label(root, text="Matric Number:").grid(row=1, column=0, padx=10, pady=8, sticky="w")
    tk.Label(root, text="Department:").grid(row=2, column=0, padx=10, pady=8, sticky="w")

    name_entry = tk.Entry(root, width=30)
    matric_entry = tk.Entry(root, width=30)
    dept_entry = tk.Entry(root, width=30)

    name_entry.grid(row=0, column=1, padx=10, pady=8)
    matric_entry.grid(row=1, column=1, padx=10, pady=8)
    dept_entry.grid(row=2, column=1, padx=10, pady=8)

    tk.Button(
        root,
        text="Submit",
        command=lambda: submit_details(name_entry, matric_entry, dept_entry),
    ).grid(row=3, column=0, columnspan=2, pady=15)

    root.mainloop()


if __name__ == "__main__":
    main()