import tkinter as tk
from tkinter import messagebox


def calculate(op, entry_num1, entry_num2, entry_result):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if op == "+":
            res = num1 + num2
        elif op == "-":
            res = num1 - num2
        elif op == "*":
            res = num1 * num2
        elif op == "/":
            if num2 == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero.")
                return
            res = num1 / num2
        elif op == "%":
            if num2 == 0:
                messagebox.showerror("Math Error", "Cannot modulo by zero.")
                return
            res = num1 % num2

        output = int(res) if res.is_integer() else round(res, 6)
        entry_result.config(state="normal")
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(output))
        entry_result.config(state="readonly")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


def clear_fields(entry_num1, entry_num2, entry_result):
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    entry_result.config(state="normal")
    entry_result.delete(0, tk.END)
    entry_result.config(state="readonly")


def main():
    root = tk.Tk()
    root.title("Swing Arithmetics")
    root.geometry("320x320")

    tk.Label(root, text="First Number").grid(row=0, column=0, padx=10, pady=8, sticky="w")
    tk.Label(root, text="Second Number").grid(row=1, column=0, padx=10, pady=8, sticky="w")
    tk.Label(root, text="Result").grid(row=2, column=0, padx=10, pady=8, sticky="w")

    entry_num1 = tk.Entry(root, width=18, justify="right")
    entry_num2 = tk.Entry(root, width=18, justify="right")
    entry_result = tk.Entry(root, width=18, justify="right", state="readonly")

    entry_num1.grid(row=0, column=1, padx=10, pady=8)
    entry_num2.grid(row=1, column=1, padx=10, pady=8)
    entry_result.grid(row=2, column=1, padx=10, pady=8)

    ops = [
        ("+", 3, 0), ("-", 3, 1),
        ("*", 4, 0), ("/", 4, 1),
        ("%", 5, 0),
    ]

    for symbol, r, c in ops:
        tk.Button(
            root,
            text=symbol,
            width=14,
            command=lambda s=symbol: calculate(s, entry_num1, entry_num2, entry_result),
        ).grid(row=r, column=c, padx=6, pady=5)

    tk.Button(
        root,
        text="CLEAR",
        width=14,
        command=lambda: clear_fields(entry_num1, entry_num2, entry_result),
    ).grid(row=5, column=1, padx=6, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()