
class Stack:
    def __init__(t):
        t.stack = []

    def push(t, data):
        t.stack.append(data)

    def pop(t):
        return t.stack.pop() if t.stack else None

    def top(t):
        return t.stack[-1] if t.stack else None

    def search(t, data):
        return t.stack.index(data) if data in t.stack else -1

    def display(t):
        print("Stack:", t.stack)

def main():
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.display()

    print("Popped:", s.pop())
    s.display()

    print("Top of stack:", s.top())

    print("Search 20:", s.search(20))
    print("Search 50:", s.search(50))

    s.display()

if __name__ == "__main__":
    main()
