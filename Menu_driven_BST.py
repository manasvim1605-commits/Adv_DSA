
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
            return
        arr=[]
        cnt=0
        level=0
        arr.append(rt)
        while(cnt<len(arr)):
            node_count=len(arr)-cnt
            print("\nLevel NO: ",level,end=" ")
            for i in range(node_count):
                temp=arr[cnt]
                cnt+=1
                print(temp.data,end=" ")
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

    # Search a node
    def search(self,rt,key):
        if rt is None:
            return False
        if rt.data == key:
            return True
        elif key < rt.data:
            return self.search(rt.left,key)
        else:
            return self.search(rt.right,key)

    # Count total number of nodes
    def count_nodes(self,rt):
        if rt is None:
            return 0
        else:
            return 1 + self.count_nodes(rt.left) + self.count_nodes(rt.right)

    # Find minimum value
    def find_min(self,rt):
        while rt.left is not None:
            rt=rt.left
        return rt

    # Delete a node
    def delete(self,rt,key):
        if rt is None:
            return rt

        if key < rt.data:
            rt.left = self.delete(rt.left,key)

        elif key > rt.data:
            rt.right = self.delete(rt.right,key)

        else:
            if rt.left is None:
                return rt.right
            elif rt.right is None:
                return rt.left

            temp = self.find_min(rt.right)
            rt.data = temp.data
            rt.right = self.delete(rt.right,temp.data)

        return rt


# Object calling part

b1=BST()

while True:
    print("\n\n----- BST MENU -----")
    print("1. Insert Node")
    print("2. Inorder Traversal")
    print("3. Preorder Traversal")
    print("4. Postorder Traversal")
    print("5. Level Wise Display")
    print("6. Search Node")
    print("7. Delete Node")
    print("8. Count Total Nodes")
    print("9. Exit")

    ch=int(input("Enter your choice: "))

    if ch==1:
        value=int(input("Enter the value of node: "))
        b1.insert(Node(value))
        print("Node inserted successfully")

    elif ch==2:
        print("Inorder:")
        b1.inorder(b1.root)

    elif ch==3:
        print("Preorder:")
        b1.preorder(b1.root)

    elif ch==4:
        print("Postorder:")
        b1.postorder(b1.root)

    elif ch==5:
        print("Level Wise Display:")
        b1.level_order(b1.root)

    elif ch==6:
        value=int(input("Enter the value to search: "))
        if b1.search(b1.root,value):
            print("Node found")
        else:
            print("Node not found")

    elif ch==7:
        value=int(input("Enter the value to delete: "))
        if b1.search(b1.root,value):
            b1.root=b1.delete(b1.root,value)
            print("Node deleted successfully")
        else:
            print("Node not found")

    elif ch==8:
        print("Total number of nodes:",b1.count_nodes(b1.root))

    elif ch==9:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")
