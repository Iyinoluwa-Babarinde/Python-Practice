import tkinter as tk
from tkinter import messagebox


def on_submit(entry_name, entry_matric, entry_dept):
    name = entry_name.get().strip()
    matric = entry_matric.get().strip()
    dept = entry_dept.get().strip()

    if not name or not matric or not dept:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    summary = f"Name: {name}\nMatric Number: {matric}\nDepartment: {dept}"
    messagebox.showinfo("Student Information", summary)

    # Bonus: Save entered details to a .txt file
    with open("students_record.txt", "a", encoding="utf-8") as file:
        file.write(summary + "\n====================\n")


def main():
    root = tk.Tk()
    root.title("Student Information GUI")
    root.geometry("400x200")

    tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=8, sticky="w")
    tk.Label(root, text="Matric Number:").grid(row=1, column=0, padx=10, pady=8, sticky="w")
    tk.Label(root, text="Department:").grid(row=2, column=0, padx=10, pady=8, sticky="w")

    entry_name = tk.Entry(root, width=28)
    entry_matric = tk.Entry(root, width=28)
    entry_dept = tk.Entry(root, width=28)

    entry_name.grid(row=0, column=1, padx=10, pady=8)
    entry_matric.grid(row=1, column=1, padx=10, pady=8)
    entry_dept.grid(row=2, column=1, padx=10, pady=8)

    tk.Button(
        root,
        text="Submit",
        command=lambda: on_submit(entry_name, entry_matric, entry_dept),
    ).grid(row=3, column=0, columnspan=2, pady=15)

    root.mainloop()


if __name__ == "__main__":
    main()