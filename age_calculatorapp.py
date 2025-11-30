import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get()) / 100

        
        simple_interest = principal * rate * time

        
        compound_amount = principal * ((1 + rate) ** time)
        compound_interest = compound_amount - principal

        result_text = (
            f"Simple Interest: {simple_interest:.2f}\n"
            f"Compound Interest: {compound_interest:.2f}\n"
            f"Total Compound Amount: {compound_amount:.2f}"
        )

        messagebox.showinfo("Results", result_text)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")


window = tk.Tk()
window.title("Interest Calculator App")
window.geometry("350x300")
window.config(padx=20, pady=20)


tk.Label(window, text="Principal Amount:").pack(anchor="w")
principal_entry = tk.Entry(window, width=25)
principal_entry.pack()

tk.Label(window, text="Time Period (years):").pack(anchor="w")
time_entry = tk.Entry(window, width=25)
time_entry.pack()

tk.Label(window, text="Rate of Interest (%):").pack(anchor="w")
rate_entry = tk.Entry(window, width=25)
rate_entry.pack()


calculate_btn = tk.Button(window, text="Calculate Interest", command=calculate_interest)
calculate_btn.pack(pady=15)


window.mainloop()
