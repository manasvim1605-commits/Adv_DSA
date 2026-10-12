#Singly linear linked list
class Node:
    def __init__(self,value):
        self.data=value #node creation
        self.next=None #node creation
class SLL: #Singly linked list creation
    def __init__(self):
        self.head=None
    def append(self, new_node): 
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
list1=SLL()
n1=Node(10)
n2=Node(20)
list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.print()