string  = []
string = input("Enter a string separated by a space: ").split()
print(string)
string.sort()
print(string)

print()
string = input("Enter a new string: ")
if string == string[::-1]:
    print("It is a pallindrome")
else:
    print("It is not a pallindrome")

print()
string = input("Enter a string: ")
count = 0
for i in string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
print("Number of vowels is:", count)
