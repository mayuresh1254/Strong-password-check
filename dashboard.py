import tkinter as tk
from tkinter import messagebox
import sqlite3
from utils import generate_password, check_strength

def open_dashboard(user_email):
    dash = tk.Toplevel()
    dash.title("Dashboard")
    dash.geometry("500x500")

    tk.Label(dash, text=f"Welcome {user_email}",
             font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(dash, text="Generate Password").pack()
    gen_entry = tk.Entry(dash, width=30)
    gen_entry.pack()

    tk.Button(dash, text="Generate",
              command=lambda: gen_entry.insert(0, generate_password())).pack(pady=5)

    tk.Label(dash, text="Check Strength").pack()
    strength_entry = tk.Entry(dash, width=30)
    strength_entry.pack()

    tk.Button(dash, text="Check",
              command=lambda: messagebox.showinfo("Strength",
                                                  check_strength(strength_entry.get()))
              ).pack(pady=5)

    def save_password():
        pwd = gen_entry.get()
        conn = sqlite3.connect("securepass.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO vault (user_email, saved_password) VALUES (?, ?)",
                       (user_email, pwd))
        conn.commit()
        conn.close()
        messagebox.showinfo("Saved", "Password saved!")

    tk.Button(dash, text="Save to Vault",
              command=save_password).pack(pady=5)

    def view_vault():
        conn = sqlite3.connect("securepass.db")
        cursor = conn.cursor()
        cursor.execute("SELECT saved_password FROM vault WHERE user_email=?", (user_email,))
        records = cursor.fetchall()
        conn.close()

        passwords = "\n".join([r[0] for r in records])
        messagebox.showinfo("Vault", passwords if passwords else "No saved passwords")

    tk.Button(dash, text="View Vault",
              command=view_vault).pack(pady=5)

    tk.Button(dash, text="Logout", command=dash.destroy).pack(pady=20)
