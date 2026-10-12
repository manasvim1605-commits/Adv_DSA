
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        

# Creating a Linked List
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            value = int(input("Enter value: "))
            new_node = Node(value)

            if self.head is None:
                self.head = new_node
            else:
                current = self.head

                while current.next is not None:
                    current = current.next

                current.next = new_node

    # Traversing the list
    def traverse(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

#   Inserting a node at a specific position  
    def insert(self, value, position):
        new_node = Node(value)

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 1

        while current is not None and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Invalid position")
            return

        new_node.next = current.next
        current.next = new_node
        
# Finding middle node
    
    def find_middle(self):
        if self.head is None:
            print("Linked list is empty")
            return

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)

# Deleting a node
    
    def delete(self, position):
        if position < 1 or self.head is None:
            print("Invalid position or empty list")
            return

        if position == 1:
            self.head = self.head.next
            return

        current = self.head
        count = 1

        while current.next is not None and count < position - 1:
            current = current.next
            count += 1

        if current.next is None:
            print("Invalid position")
            return

        current.next = current.next.next

# Reversing list   
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

# Calculating the sum of every two consecutive node values.   
    def sum(self):
        current = self.head

        if current is None or current.next is None:
            print("At least two nodes are required")
            return

        while current.next is not None:
            total = current.data + current.next.data

            print(current.data, "+", current.next.data, "=", total)

            current = current.next


ll = LinkedList()
ll.create()
print("Inserting value and traversing the list")
ll.insert(25, 3)
ll.traverse()
print("Finding middle node")
ll.find_middle()
print("Deleting node")
ll.delete(2)
ll.traverse()
print("Reversing the list")
ll.reverse()
ll.traverse()
print("Calculating the sum of every two consecutive node values")
ll.sum()