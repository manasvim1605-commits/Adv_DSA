
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        temp = self.top
        self.top = self.top.next
        return temp.data
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, new_node):
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def print(self):
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next
    def reverse(self):
        st1 = Stack()
        st2 = Stack()
        temp = self.front
        while temp:
            st1.push(Node(temp.data))
            temp = temp.next
        while st1.top:
            st2.push(Node(st1.pop()))
        while st2.top:
            st1.push(Node(st2.pop()))
        self.front = None
        self.rear = None
        while st1.top:
            self.enqueue(Node(st1.pop()))
q = Queue()
q.enqueue(Node(10))
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))
print("Original Queue:")
q.print()
q.reverse()
print("Reversed Queue:")
q.print()