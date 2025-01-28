def perfect(num):
        sum = 0
        for i in range(1, num):
                if num % i == 0:
                        sum += i
        if sum == num:
                print("It is a perfect number.")
        else:
                print("Not a perfect number.")

def main():
        number = int(input("Enter any number: "))
        perfect(number)

main()

