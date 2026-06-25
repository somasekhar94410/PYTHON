from tkinter import *
from tkinter import messagebox

def calculate_bill():
    try:
        units = float(units_entry.get())
        rate = float(rate_entry.get())

        bill = units * rate

        result_label.config(
            text=f"Bill Amount: ₹ {bill:.2f}"
        )

    except:
        messagebox.showerror("Error", "Please enter valid numbers")

root = Tk()
root.title("Current Bill Generator")
root.geometry("450x350")
root.config(bg="#1e1e1e")

title = Label(
    root,
    text="Electricity Bill Generator",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="cyan"
)
title.pack(pady=15)

Label(
    root,
    text="Units Consumed",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
).pack()

units_entry = Entry(root, font=("Arial", 12))
units_entry.pack(pady=5)

Label(
    root,
    text="Rate Per Unit",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
).pack()

rate_entry = Entry(root, font=("Arial", 12))
rate_entry.pack(pady=5)

Button(
    root,
    text="Calculate Bill",
    font=("Arial", 12, "bold"),
    bg="#00c853",
    fg="white",
    command=calculate_bill
).pack(pady=20)

result_label = Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#1e1e1e",
    fg="yellow"
)
result_label.pack()

root.mainloop()