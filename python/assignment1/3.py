class Queue:
    def __init__(t):
        t.queue = []

    def insert(t, data):
        t.queue.append(data)

    def remove(t):
        return t.queue.pop(0) if t.queue else None

    def search(t, data):
        return t.queue.index(data) if data in t.queue else -1

    def display(t):
        print("Queue:", t.queue)

def main():
    q = Queue()

    q.insert(10)
    q.insert(20)
    q.insert(30)
    q.insert(40)
    q.display()

    print("Removed:", q.remove())
    q.display()

    print("Search 20:", q.search(20))
    print("Search 50:", q.search(50))  

    q.display()

if __name__ == "__main__":
    main()