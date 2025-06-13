from array import *

def isPrime(num):
    if num > 1:
        for i in range(2, (num//2)+1):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

arr = array('i')
size = int(input('Enter a size for the array: '))
for i in range(size):
        arr.append(int(input('Enter number: ')))
print("Original:", arr)
for i in arr:
    if isPrime(i):
        arr.remove(i)
print("After removal of prime numbers:", arr)
