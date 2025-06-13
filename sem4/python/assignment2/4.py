import threading

def print_odd():
    for i in range(1, 11, 2):
        print("Odd:", i)

def print_even():
    for i in range(2, 11, 2):
        print("Even:", i)

t1 = threading.Thread(target=print_odd)
t2 = threading.Thread(target=print_even)

t1.start()
t2.start()

t1.join()
t2.join()
