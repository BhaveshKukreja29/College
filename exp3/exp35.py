import operations

nums = []
size = int(input("How many elements you want to append? "))
for i in range(size):
        nums.append(int(input(f"Enter element {i + 1}: ")))
print(f"List looks like: {nums}")
print()

print("Enter 1 to have sum of elements of list")
print("Enter 2 to have product of elements of list.")
print("Enter 3 to sum the elements at even indices.")
print("Enter 4 to append elements in list")
print()

opt = int(input("Enter choice: "))

if opt == 1:
        print("Sum of elements is:", operations.summation(nums))
elif opt == 2:
        print("Product of elements is: ", operations.product(nums))
elif opt == 3:
        print("Sum at even indices is: ", opertations.sumEven(nums))
elif opt == 4:
        nums.append(int(input("Enter number: ")))
        print(nums)
else:
        print("Enter valid option") 
