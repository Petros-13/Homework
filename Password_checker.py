import tkinter as tk
from tkinter import messagebox
import re

def check_strength():
    password = password_entry.get()

    if len(password) == 0:
        messagebox.showwarning("Empty", "Please enter a password!")
        return

    strength = ""

   
    length = len(password) >= 8
    lowercase = re.search(r"[a-z]", password)
    uppercase = re.search(r"[A-Z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password)

    score = sum([length, bool(lowercase), bool(uppercase), bool(digit), bool(special)])

    if score <= 2:
        strength = "Weak Password"
        color = "red"
    elif score == 3 or score == 4:
        strength = "Medium Password"
        color = "orange"
    else:
        strength = "Strong Password"
        color = "green"

    result_label.config(text=strength, fg=color)




window = tk.Tk()
window.title("Password Strength Checker App")
window.geometry("400x400")
window.resizable(False, False)

title_label = tk.Label(window, text="Password Strength Checker", font=("Arial", 16, "bold"))
title_label.pack(pady=20)


tk.Label(window, text="Enter Password:", font=("Arial", 12)).pack()
password_entry = tk.Entry(window, width=30, show="*")
password_entry.pack(pady=10)


check_button = tk.Button(window, text="Check Strength", command=check_strength, width=15)
check_button.pack(pady=10)


result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=20)

window.mainloop()
