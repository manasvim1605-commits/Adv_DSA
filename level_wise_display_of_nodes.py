# Binary Search Tree (BST)
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None 
class BST: 
    def __init__(self):
        self.root = None       
    def insert(self,new_node):
        if self.root is None:  #BST is empty
            self.root = new_node
        else:
            temp=self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp=temp.right
    def inorder(self,rt): 
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data,end=" ")
            self.inorder(rt.right)
    def level_order(self,rt):
        if rt is None:
            print("BST is empty")
        arr=[]
        cnt=0
        level=0
        arr.append(rt)
        while(cnt<len(arr)):
            node_count=len(arr)-cnt #level wise node count
            print("\nLevel NO: ",level,end=" ")
            for i in range(node_count):
                temp=arr[cnt]
                cnt+=1
                print(temp.data,end=" ") #visiting node
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            level+=1
    def preorder(self,rt):        
        if rt is None:
            return
        else:
            print(rt.data,end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)
    def postorder(self,rt):        
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data,end=" ")

b1=BST()
b1.insert(Node(100))
b1.insert(Node(10)) 
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))
print("Inorder:")
b1.inorder(b1.root)             
print("\nPreorder:")
b1.preorder(b1.root)             
print("\nPostorder:")
b1.postorder(b1.root)
print("\nLevel order")
b1.level_order(b1.root)