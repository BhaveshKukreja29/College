import numpy as np

def create_array():
    return np.array(list(map(int, input("Enter elements: ").split())))

def create_arange():
    start, stop, step = map(int, input("Enter start, stop, step: ").split())
    return np.arange(start, stop, step)

def sum_array(arr):
    return np.sum(arr)

def sort_array(arr):
    return np.sort(arr)

def compare_arrays(arr1, arr2):
    return np.array_equal(arr1, arr2)

while True:
    print("\nMenu:")
    print("1. Create array")
    print("2. Create using arange()")
    print("3. Sum of array")
    print("4. Sort array")
    print("5. Compare two arrays")
    print("6. Exit")

    choice = int(input("Enter choice: "))
    
    if choice == 1:
        arr = create_array()
        print("Array:", arr)
    elif choice == 2:
        arr = create_arange()
        print("Array:", arr)
    elif choice == 3:
        print("Sum:", sum_array(arr))
    elif choice == 4:
        print("Sorted array:", sort_array(arr))
    elif choice == 5:
        arr2 = create_array()
        print("Arrays are equal:", compare_arrays(arr, arr2))
    elif choice == 6:
        break
    else:
        print("Invalid choice")
