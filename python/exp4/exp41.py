import list_operations

nums = []
size = int(input("How many elements you want to append? "))
for i in range(size):
    nums.append(int(input(f"Enter element {i + 1}: ")))
print(f"List looks like: {nums}")

while True:
    print()
    print("Enter 1 to put even and odd elements in different lists")
    print("Enter 2 to merge and sort two lists")
    print("Enter 3 to update first element")
    print("Enter 4 to print middle element")
    print("Enter 5 to exit")
    print()
    opt = int(input("Enter choice: "))

    if opt == 1:
        even_list = []
        odd_list = []
        for num in nums:
            if num % 2 == 0:
                even_list.append(num)
            else:
                odd_list.append(num)
        print("Even list:", even_list)
        print("Odd list:", odd_list)

    elif opt == 2:
        list1 = nums
        size2 = int(input("Enter size of second list: "))
        list2 = []
        for i in range(size2):
            list2.append(int(input(f"Enter element {i + 1}: ")))
        merged_list = list1 + list2
        merged_list.sort()
        print("Merged and sorted list:", merged_list)

    elif opt == 3:
        x = int(input("Enter value to update first element: "))
        nums[0] = x
        print("Updated list:", nums)

    elif opt == 4:
        mid = len(nums) // 2
        print("Middle element:", nums[mid])

    elif opt == 5:
        print("Exiting program...")
        break

    else:
        print("Enter valid option")
