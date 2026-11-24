import tkinter as tk


def show_biodata(entry_name, text_address, entry_occupation, entry_age, text_output):
    name = entry_name.get()
    address = text_address.get("1.0", tk.END).strip()
    occupation = entry_occupation.get()
    age = entry_age.get()

    result = (
        f"Name: {name}\n"
        f"Address: {address}\n"
        f"Occupation: {occupation}\n"
        f"Age: {age}"
    )

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)


def main():
    root = tk.Tk()
    root.title("BIODATA FORM")
    root.geometry("460x380")
    root.configure(bg="#19c35a")

    form = tk.Frame(root, bg="#ececec", padx=15, pady=15)
    form.pack(fill="both", expand=True, padx=10, pady=10)

    tk.Label(form, text="Name", bg="#ececec").grid(row=0, column=0, sticky="w", pady=5)
    entry_name = tk.Entry(form, width=25)
    entry_name.grid(row=0, column=1, sticky="w", pady=5)

    tk.Label(form, text="Address", bg="#ececec").grid(row=1, column=0, sticky="w", pady=5)
    text_address = tk.Text(form, width=25, height=4)
    text_address.grid(row=1, column=1, sticky="w", pady=5)

    tk.Label(form, text="Occupation", bg="#ececec").grid(row=2, column=0, sticky="w", pady=5)
    entry_occupation = tk.Entry(form, width=25)
    entry_occupation.grid(row=2, column=1, sticky="w", pady=5)

    tk.Label(form, text="Age", bg="#ececec").grid(row=3, column=0, sticky="w", pady=5)
    entry_age = tk.Entry(form, width=12)
    entry_age.grid(row=3, column=1, sticky="w", pady=5)

    tk.Label(form, text="Output", bg="#ececec").grid(row=4, column=0, sticky="nw", pady=5)
    text_output = tk.Text(form, width=28, height=6)
    text_output.grid(row=4, column=1, sticky="w", pady=5)

    tk.Button(
        form,
        text="OK",
        width=10,
        command=lambda: show_biodata(
            entry_name, text_address, entry_occupation, entry_age, text_output
        ),
    ).grid(row=0, column=2, padx=15, pady=5)

    tk.Button(form, text="Exit", width=10, command=root.destroy).grid(
        row=1, column=2, padx=15, pady=5, sticky="n"
    )

    root.mainloop()


if __name__ == "__main__":
    main()