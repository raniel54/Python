import tkinter as tk
import sqlite3


class Login:
    def __init__(self, master):
        self.master = master
        master.title("Login")

        self.label_username = tk.Label(master, text="Usuário:")
        self.label_password = tk.Label(master, text="Senha:")

        self.entry_username = tk.Entry(master)
        self.entry_password = tk.Entry(master, show="*")

        self.label_username.grid(row=0, sticky=tk.E)
        self.label_password.grid(row=1, sticky=tk.E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.logbtn = tk.Button(master, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.db_conn = sqlite3.connect("login.db")
        self.db_cursor = self.db_conn.cursor()
        self.db_cursor.execute(
            """CREATE TABLE IF NOT EXISTS users
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT NOT NULL,
                            password TEXT NOT NULL);"""
        )

    def _login_btn_clicked(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        self.db_cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password),
        )
        user = self.db_cursor.fetchone()

        if user:
            print("Login realizado com sucesso!")
        else:
            print("Usuário ou senha incorretos.")


root = tk.Tk()
login = Login(root)
root.mainloop()
