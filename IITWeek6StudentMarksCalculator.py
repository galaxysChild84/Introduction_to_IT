import tkinter as tk
from tkinter import messagebox

def calculate_result():
    try:
        # Split the input into a list of numbers
        raw = marks_entry.get().split()
        marks = [float(m) for m in raw]

        if len(marks) == 0:
            messagebox.showerror("Error", "Please enter at least one mark.")
            return

        average = sum(marks) / len(marks)
        status = "Passed" if average >= 50 else "Failed"

        # Update result label
        result_label.config(text=f"Average: {average:.2f} — {status}")

        # Change background colour
        if status == "Passed":
            result_label.config(bg="lightgreen")
        else:
            result_label.config(bg="salmon")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers only.")

def clear_fields():
    marks_entry.delete(0, tk.END)
    result_label.config(text="", bg=default_bg)


app = tk.Tk()
app.title("Teacher Mark Calculator")

default_bg = app.cget("bg")

tk.Label(app, text="Enter marks (separated by spaces):").pack(pady=5)

marks_entry = tk.Entry(app, width=40)
marks_entry.pack(pady=5)

tk.Button(app, text="Calculate", command=calculate_result).pack(pady=5)
tk.Button(app, text="Clear", command=clear_fields).pack(pady=5)

result_label = tk.Label(app, text="", font=("Arial", 14), width=30)
result_label.pack(pady=10)

app.mainloop()
