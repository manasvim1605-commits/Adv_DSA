class Node:
    def __init__(self,pid,name,pr):
        self.pid=pid
        self.name=name
        self.priority=pr
        self.next=None
class PQ:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.front==None:
            self.front=self.rear=new_node
            return
        if self.front.priority > new_node.priority: #checks the priority of 1st node with new_node
            new_node=self.front
            self.front=new_node
            return
        else:
            temp=self.front
            while temp:
                if new_node.priority < temp.priority: #traverse and then insert
                    break
                else:
                    prev=temp
                    temp=temp.next 
                    prev.next=new_node
                    new_node.next=temp
            if temp==None: #end of queue
                self.rear=new_node
    def dequeue(self):
        if self.front:
            temp=self.front
            print("Executing process with PID: ",temp.pid," and Name: ",temp.name)
            self.front=self.front.next
            if self.front==None:
                self.rear=None
            else:
                print("Queue is empty")
    def display_next(self):
        if self.front:
            print("Next process in the Queue with PID: ",self.front.pid," and Name: ",self.front.name)
        else:
            print("No pending process")
    def display_all(self):
        temp=self.front
        if temp==None:
            print("Queue is empty")
            return
        while temp:
            print(temp.pid,temp.name,temp.priority)
            temp=temp.next 
    def count(self):
        temp=self.front
        cnt=0
        while temp:
            cnt=cnt+1
            temp=temp.next
        print("Total pending process: ",cnt)
pq=PQ()
pq.enqueue(Node(100,"System Process",1))
pq.enqueue(Node(101,"Low priority",4))
pq.enqueue(Node(102,"Background Process",3))
pq.enqueue(Node(103,"Interactive Process",2))

print("All processes: ")
pq.display_all()

print("\nNext Process: ")
pq.display_next()

print("\nExectuing Process: ")
pq.dequeue()

print("All pending processes: ")
pq.display_all()

print("\nCounting processes: ")
pq.count()
