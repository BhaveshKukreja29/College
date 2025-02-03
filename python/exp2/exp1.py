from array import *

arr = array('i')
size = int(input('Enter a size for the array: '))

for i in range(size):
        arr.append(int(input('Enter number: ')))
print(arr)
arr.reverse()
print('Reverse order:', arr)
print('Size in bytes of one item:', arr.itemsize)
print()
arr2 = array('i')
size2 = int(input('Enter size for array 2: '))
for i in range(size2):
        arr2.append(int(input('Enter number: ')))

arr.extend(arr2)
print('New array:', arr)
print()
dele = int(input('Enter the index of element to be deleted: '))

arr.remove(arr[dele])

print('Array after deletion:', arr)

