class Node:
    def __init__(t, data):
        t.data = data
        t.next = None


class LinkedList:
    def __init__(t):
        t.head = None

    def display(t):
        temp = t.head
        print("Linked List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def insert_at_beginning(t, data):
        new_node = Node(data)
        new_node.next = t.head
        t.head = new_node

    def insert_at_end(t, data):
        new_node = Node(data)
        if not t.head:
            t.head = new_node
            return
        temp = t.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(t, pos, data):
        if pos == 0:
            t.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = t.head
        for _ in range(pos - 1):
            if not temp:
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_from_beginning(t):
        if t.head:
            t.head = t.head.next

    def delete_from_end(t):
        if not t.head:
            return
        if not t.head.next:
            t.head = None
            return
        temp = t.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_at_position(t, pos):
        if pos == 0 and t.head:
            t.head = t.head.next
            return
        temp = t.head
        for _ in range(pos - 1):
            if not temp.next:
                return
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    def delete_element(t, value):
        temp = t.head
        if temp and temp.data == value:
            t.head = temp.next
            return
        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def search(t, value):
        temp = t.head
        pos = 0
        while temp:
            if temp.data == value:
                return pos
            temp = temp.next
            pos += 1
        return -1

    def replace(t, pos, value):
        temp = t.head
        for _ in range(pos):
            if not temp:
                return
            temp = temp.next
        if temp:
            temp.data = value

    def forward_traversal(t):
        t.display()

    def reverse_traversal(t):
        def _reverse(node):
            if node is None:
                return
            _reverse(node.next)
            print(node.data, end=" -> ")
        print("Reverse Traversal:", end=" ")
        _reverse(t.head)
        print("None")

    def insert_after_element(t, key, data):
        temp = t.head
        while temp:
            if temp.data == key:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

def main():
    ll = LinkedList()

    ll.insert_at_beginning(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_position(1, 15) 
    ll.insert_after_element(20, 25)  

    ll.display()

    ll.delete_from_beginning()
    ll.display()

    ll.delete_from_end()
    ll.display()

    ll.delete_at_position(1)
    ll.display()

    ll.delete_element(20)
    ll.display()

    print("Search 15:", ll.search(15))
    print("Search 100:", ll.search(100)) 

    ll.replace(0, 99)
    ll.display()

    ll.forward_traversal()
    ll.reverse_traversal()

if __name__ == "__main__":
    main()