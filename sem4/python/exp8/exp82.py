"""
Python program to demonstrate use of regular expression 

● Create a phone list using file (surname name number)

Find all the entries of phone book with surname as “Rao” and first name starting with 
‘J’ or ‘K'
"""
import re

with open("phonebook.txt", "w") as f:
    f.write("Williams John 9876543210\n")
    f.write("Rao Kevin 8765432109\n")
    f.write("Sharma Amit 7654321098\n")
    f.write("Rao Kiran 6543210987\n")
    f.write("Rao Rohit 5432109876\n")
    f.write("Mulchandani Michael 4321098765\n")
    f.write("Rao Jack 3210987654\n")

with open("phonebook.txt", "r") as f:
    print("\nEntries matching criteria :\n")
    found = False

    for line in f:
        if re.match(r"^Rao\s+[JK]\w*\s+\d+$", line, re.I):
            print(line.strip())
            found = True

    if not found:
        print("No matching entries found.")
