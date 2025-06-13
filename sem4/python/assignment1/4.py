from collections import deque


class DequeWrapper:
    def __init__(t):
        t.deque = deque()

    def add_front(t, data):
        t.deque.appendleft(data)

    def remove_front(t):
        return t.deque.popleft() if t.deque else None

    def add_rear(t, data):
        t.deque.append(data)

    def remove_rear(t):
        return t.deque.pop() if t.deque else None

    def search(t, data):
        return t.deque.index(data) if data in t.deque else -1

    def display(t):
        print("Deque:", list(t.deque))

def main():
    dq = DequeWrapper()

    dq.add_front(10)
    dq.add_rear(20)
    dq.add_front(5)
    dq.add_rear(30)
    dq.display()

    print("Removed from front:", dq.remove_front())
    dq.display()

    print("Removed from rear:", dq.remove_rear())
    dq.display()

    print("Search 10:", dq.search(10))
    print("Search 50:", dq.search(50))  

    dq.display()

if __name__ == "__main__":
    main()
