for i in range(100000):
    dig = []
    num = i
    sum = 0
    while num != 0:
        dig.append(num % 10)
        num //= 10
    power = len(dig)

    for j in dig:
        sum += pow(j, power)
    if sum == i:
        print(i)
