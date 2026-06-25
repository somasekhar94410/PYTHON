from tkinter import *
from tkinter import messagebox

def check_eligibility():
    try:
        name = name_entry.get()
        age = int(age_entry.get())
        percentage = float(percentage_entry.get())

        if age >= 18 and percentage >= 60:
            result.config(
                text=f"{name}\nEligible for Recruitment",
                fg="green"
            )
        else:
            result.config(
                text=f"{name}\nNot Eligible for Recruitment",
                fg="red"
            )

    except:
        messagebox.showerror("Error", "Enter valid details")

root = Tk()
root.title("Recruitment Screening System")
root.geometry("500x450")
root.configure(bg="#1E1E1E")

title = Label(
    root,
    text="Recruitment Screening System",
    font=("Arial", 18, "bold"),
    bg="#1E1E1E",
    fg="cyan"
)
title.pack(pady=20)

Label(root, text="Candidate Name",
      bg="#1E1E1E", fg="white",
      font=("Arial", 12)).pack()

name_entry = Entry(root, font=("Arial", 12), width=30)
name_entry.pack(pady=5)

Label(root, text="Age",
      bg="#1E1E1E", fg="white",
      font=("Arial", 12)).pack()

age_entry = Entry(root, font=("Arial", 12), width=30)
age_entry.pack(pady=5)

Label(root, text="Percentage",
      bg="#1E1E1E", fg="white",
      font=("Arial", 12)).pack()

percentage_entry = Entry(root, font=("Arial", 12), width=30)
percentage_entry.pack(pady=5)

Button(
    root,
    text="Check Eligibility",
    font=("Arial", 12, "bold"),
    bg="#00C853",
    fg="white",
    command=check_eligibility
).pack(pady=20)

result = Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#1E1E1E"
)
result.pack(pady=20)

root.mainloop()