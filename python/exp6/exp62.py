"""
Python program to
● create a file
● count no. of lines , words and characters in a file.
● write content of a file in a new file and read that new file.
"""
from sys import argv, exit

def main():
    if len(argv) != 2:
        print('Please enter only 3 arguments')
        print("Example Usage: python3 exp62.py <Your file name here or it's path>")
        exit(1)

    if not argv[1].endswith('.py'):
        print('Not a python file')
        exit(1)

    try:
        with open(argv[1], 'r') as file:
            lines = file.readlines()

        count = 0
        countchar = 0
        countword = 0
        for line in lines:
            line = line.strip()
        
            count += 1

            countchar += sum(1 for char in line if char != " ")
            
            countword += len(line.split())

        print('Number of Lines:', count)
        print('Number of Words:', countword)
        print('Number of Characters:', countchar)

    except FileNotFoundError:
        print('Could not locate the file')
        exit(1)

if __name__ == "__main__":
    main()