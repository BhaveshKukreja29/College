"""
Python program to demonstrate use of Tkinter interface module.
Create a GUI based application using widgets Entry, Label, Text, Button, RadioButton,
CheckButton, ListBox, Menu, Spinbox (any five).
Save the details in a file and read back from file on python prompt.
"""
import tkinter as tk

root = tk.Tk()

root.title("User Information Form")
root.geometry("400x400")

tk.Label(root, text="Name:").pack()
nameEntry = tk.Entry(root)
nameEntry.pack()

genderVar = tk.StringVar(value="None")

tk.Label(root, text="Gender:").pack()
tk.Radiobutton(root, text="Male", variable=genderVar, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=genderVar, value="Female").pack()


tk.Label(root, text="Select category:").pack()
category = tk.Listbox(root)
for c in ["Student", "Professional", "Other"]:
    category.insert(tk.END, c)
category.pack()

tk.Label(root, text="Age:").pack()
age_spinbox = tk.Spinbox(root, from_=18, to=100)
age_spinbox.pack()


terms = tk.BooleanVar()
tk.Checkbutton(root, text="I agree to the terms", variable=terms).pack()


def on_click():
    name = nameEntry.get()
    gender = genderVar.get()
    term = "Accepted" if terms.get() else "Not Accepted"
    age = age_spinbox.get()
    cat = category.get(tk.ACTIVE)

    with open("userdata.txt", "w") as file:
        file.write(f"Name: {name}\nGender: {gender}\nAge: {age}\nCategory: {cat}\nTerms: {term}")

    print("Success", "Data saved successfully!")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

def read_data():
    try:
        with open("userdata.txt", "r") as file:
            data = file.read()
        print("User Data:\n", data)
    except FileNotFoundError:
        print("No data found. Please save data first.")

tk.Button(root, text="Read Data", command=read_data).pack()


root.mainloop()