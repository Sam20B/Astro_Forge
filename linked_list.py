class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def display(self, message=""):
        print(message, end="")
        current = self.head
        while current:
            if current.next is None:
                print(current.value, end="")
            else:
                print(current.value, end= " -> ")
            current = current.next
        print()
        
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
li = LinkedList()

li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.append(5)

li.display("Linked List: ")

li.reverse()

li.display("Reversed Linked List: ")