import tkinter as tk
from tkinter import messagebox

POUND_TO_KG = 0.453592


# Part (a): Console program
def console_converter():
    pounds = float(input("Enter weight in pounds: "))
    kilograms = pounds * POUND_TO_KG
    print(f"{kilograms:.5f} kg")


# Part (b): GUI program
def convert_weight(entry_pounds, entry_kg):
    try:
        pounds = float(entry_pounds.get())
        kg = pounds * POUND_TO_KG
        entry_kg.config(state="normal")
        entry_kg.delete(0, tk.END)
        entry_kg.insert(0, f"{kg:.5f}")
        entry_kg.config(state="readonly")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for weight.")


def gui_converter():
    root = tk.Tk()
    root.title("Form1")
    root.geometry("360x180")

    tk.Label(root, text="Enter Weight in Pounds:").grid(
        row=0, column=0, padx=12, pady=12, sticky="w"
    )
    entry_pounds = tk.Entry(root, width=20)
    entry_pounds.grid(row=0, column=1, padx=12, pady=12)

    tk.Label(root, text="Weight in Kilogram").grid(
        row=1, column=0, padx=12, pady=12, sticky="w"
    )
    entry_kg = tk.Entry(root, width=20, state="readonly")
    entry_kg.grid(row=1, column=1, padx=12, pady=12)

    tk.Button(
        root,
        text="Convert",
        command=lambda: convert_weight(entry_pounds, entry_kg),
    ).grid(row=2, column=0, columnspan=2, pady=12)

    root.mainloop()


if __name__ == "__main__":
    choice = input("Run (1) Console or (2) GUI? [1/2]: ").strip()
    if choice == "1":
        console_converter()
    else:
        gui_converter()