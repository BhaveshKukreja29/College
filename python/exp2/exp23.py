string = input('Enter a string: ')
count = 0
result = ''
for i in string:
    if i == string[0] and count != 0:
        i = '@'
    else:
        count += 1
    result += i

print('Output: ', result)
