import tkinter as tk
from auth import LoginRegisterApp
from database import init_db

init_db()

root = tk.Tk()
root.title("SecurePass Manager")
root.geometry("500x500")

app = LoginRegisterApp(root)
root.mainloop()
