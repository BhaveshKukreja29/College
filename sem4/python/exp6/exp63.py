"""
Python program to
● create a class Customer with id, name, mobile number as instance variable and
constructor to initialize these instance variables.
● Instantiate n instances of classes
● Save details of all customer in a file and read back from that file.
"""
from sys import exit

class Customer:
    def __init__(t, id, name, mno):
        t.id = id
        t.name = name
        t.mno = mno
    
    def __str__(t):
        return f"{t.id}, {t.name}, {t.mno}"
    

def main():
    filename = input("Enter the file name: ")
    try:
        f = open(filename, "x")
        f.close()
    except:
        print("File like that already exists please try again.")
        return -1
    
    f = open(filename, "a")

    n = int(input("Enter the number of Customers: "))

    for i in range(n):
        print(f'For customer {i + 1}')
        id = int(input('Enter id: '))
        name = input('Enter name: ')
        mno = int(input('Enter Mobile number: ')) 
        print()

        f.write(f'{str(Customer(id, name, mno))}\n')

    f.close()

    return 0

if __name__ == "__main__":
    while True:
        if main() == 0:
            break