import string

def pangram(text):
        text.lower()
        chars = string.ascii_lowercase
        if all(char in text for char in chars):
                print("Is a pangram")
        else:
                print("Isn't a pangram")

def main():
        text = input("Enter a string: ")
        pangram(text)

main()

