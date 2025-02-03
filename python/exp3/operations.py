def summation(lst):
        return sum(lst)


def product(lst):
        res = 1
        for i in lst:
                res *= i
        return res


def sumEven(lst):
        sum = 0
        size = len(lst) - 1
        for i in range(0, size, 2):
                sum += lst[i]
        return sum
