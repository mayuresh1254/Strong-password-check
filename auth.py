import tkinter as tk
from tkinter import messagebox
import sqlite3
import random
from utils import hash_password
from dashboard import open_dashboard

generated_otp = ""

class LoginRegisterApp:

    def __init__(self, root):
        self.root = root

        tk.Label(root, text="SecurePass Manager",
                 font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(root, text="Email").pack()
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.pack()

        tk.Label(root, text="Password").pack()
        self.password_entry = tk.Entry(root, show="*", width=30)
        self.password_entry.pack()

        tk.Label(root, text="OTP").pack()
        self.otp_entry = tk.Entry(root, width=30)
        self.otp_entry.pack()

        tk.Button(root, text="Generate OTP",
                  command=self.generate_otp).pack(pady=5)

        tk.Button(root, text="Register",
                  command=self.register).pack(pady=5)

        tk.Button(root, text="Login",
                  command=self.login).pack(pady=5)

    def generate_otp(self):
        global generated_otp
        generated_otp = str(random.randint(100000, 999999))
        messagebox.showinfo("OTP", f"Demo OTP: {generated_otp}")

    def register(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        otp = self.otp_entry.get()

        if otp != generated_otp:
            messagebox.showerror("Error", "Invalid OTP")
            return

        hashed = hash_password(password)

        conn = sqlite3.connect("securepass.db")
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (email, password_hash) VALUES (?, ?)", (email, hashed))
            conn.commit()
            messagebox.showinfo("Success", "Registration Successful")
        except:
            messagebox.showerror("Error", "User already exists")

        conn.close()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        hashed = hash_password(password)

        conn = sqlite3.connect("securepass.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=? AND password_hash=?", (email, hashed))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Login", "Login Successful")
            open_dashboard(email)
        else:
            messagebox.showerror("Login", "Invalid Credentials")
