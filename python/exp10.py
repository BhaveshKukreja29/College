"""
Python program to
● Connect to MySQL database and create a table.
● Create a GUI-based application to collect user details.
● Save details in the database and retrieve them.
● Display retrieved details in a tabular format.
"""

import mysql.connector
import tkinter as tk
from tkinter import messagebox
from os import getenv


class Database:
    def __init__(t):
        t.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=getenv("MYSQL_PASSWORD"),
            database="user_db"
        )
        t.cursor = t.conn.cursor()
        t.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age INT,
                gender VARCHAR(10),
                category VARCHAR(50),
                agreement BOOLEAN
            )
        """)
        t.conn.commit()

    def insert_user(t, name, age, gender, category, agreement):
        t.cursor.execute("INSERT INTO users (name, age, gender, category, agreement) VALUES (%s, %s, %s, %s, %s)",
                         (name, age, gender, category, agreement))
        t.conn.commit()

    def fetch_users(t):
        t.cursor.execute("SELECT * FROM users")
        return t.cursor.fetchall()

    def close(t):
        t.cursor.close()
        t.conn.close()


class UserForm:
    def __init__(t, root):
        t.db = Database()

        tk.Label(root, text="Name:").pack()
        t.name_entry = tk.Entry(root)
        t.name_entry.pack()

        tk.Label(root, text="Age:").pack()
        t.age_spinbox = tk.Spinbox(root, from_=18, to=100)
        t.age_spinbox.pack()

        tk.Label(root, text="Gender:").pack()
        t.gender_var = tk.StringVar(value="None")
        tk.Radiobutton(root, text="Male", variable=t.gender_var, value="Male").pack()
        tk.Radiobutton(root, text="Female", variable=t.gender_var, value="Female").pack()

        tk.Label(root, text="Category:").pack()
        t.category_listbox = tk.Listbox(root)
        for category in ["Student", "Professional", "Other"]:
            t.category_listbox.insert(tk.END, category)
        t.category_listbox.pack()

        t.agree_var = tk.BooleanVar()
        tk.Checkbutton(root, text="I agree to the terms", variable=t.agree_var).pack()

        tk.Button(root, text="Save Data", command=t.save_data).pack()
        tk.Button(root, text="Fetch Data", command=t.fetch_data).pack()

    def save_data(t):
        name = t.name_entry.get()
        age = t.age_spinbox.get()
        gender = t.gender_var.get()
        category = t.category_listbox.get(tk.ACTIVE)
        agreement = t.agree_var.get()

        if name and category:
            t.db.insert_user(name, age, gender, category, agreement)
            messagebox.showinfo("Success", "Data saved successfully!")
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    def fetch_data(t):
        users = t.db.fetch_users()

        print("\n+----+------------+-----+--------+------------+-----------+")
        print("| ID |    Name    | Age | Gender |  Category  | Agreement |")
        print("+----+------------+-----+--------+------------+-----------+")

        for user in users:
            print(f"|{user[0]:^4}|{user[1]:^12}|{user[2]:^5}|{user[3]:^8}|{user[4]:^12}|{str(bool(user[5])):^11}|")
            print("+----+------------+-----+--------+------------+-----------+")


def main():
    root = tk.Tk()
    root.title("User Information Form")
    root.geometry("400x400")

    app = UserForm(root)
    root.mainloop()

    return 0


if __name__ == "__main__":
    while True:
        if main() == 0:
            break