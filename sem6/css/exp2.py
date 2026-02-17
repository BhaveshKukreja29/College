def inverse(a, b):
    t1 = 0
    t2 = 1

    if a > b:
        r1 = a
        r2 = b
    else:
        r1 = b
        r2 = a

    print("Q\tR1\tR2\tR\tT1\tT2\tT")

    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        t = t1 - q * t2

        print(q, "\t", r1, "\t", r2, "\t", r, "\t", t1, "\t", t2, "\t", t)

        r1 = r2
        r2 = r
        t1 = t2
        t2 = t

    if t1 < 0:
        t1 = t1 + 26

    if r1 == 1:
        print("The multiplicative inverse of", a, "is", t1)
    else:
        print("The GCD of", a, "and", b, "is", r1)
        print("We cannot find multiplicative inverse for this number")


a = int(input("Enter the value to find the multiplicative inverse of: "))
b = int(input("Enter the 2nd number: "))

inverse(a, b)

