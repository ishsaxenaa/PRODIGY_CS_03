import tkinter as tk
from tkinter import messagebox
import re

class PasswordComplexityChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Complexity Checker")
        self.root.geometry("350x250")

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Enter Password:")
        self.label.pack(pady=10)

        self.password_entry = tk.Entry(self.root, show='*', width=30)
        self.password_entry.pack(pady=5)

        self.check_button = tk.Button(self.root, text="Check Password", command=self.check_password)
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", fg="red")
        self.result_label.pack(pady=5)

    def check_password(self):
        password = self.password_entry.get()

        feedback = self.get_password_feedback(password)
        self.result_label.config(text=feedback, fg="red" if "weak" in feedback.lower() else "green")

    def get_password_feedback(self, password):
        feedback = []

        # Criteria for a strong password
        min_length = 8
        if len(password) < min_length:
            feedback.append(f"Password must be at least {min_length} characters long.")

        if not re.search(r'[A-Z]', password):
            feedback.append("Password must contain at least 1 uppercase letter.")

        if not re.search(r'[a-z]', password):
            feedback.append("Password must contain at least 1 lowercase letter.")

        if not re.search(r'[0-9]', password):
            feedback.append("Password must contain at least 1 number.")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            feedback.append("Password must contain at least 1 special character.")

        if not feedback:
            return "Password is STRONG."
        else:
            return "Password is WEAK.\n" + "\n".join(feedback)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordComplexityChecker(root)
    root.mainloop()
