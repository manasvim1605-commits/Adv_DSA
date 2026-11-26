
# Binary Search Tree (BST)
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    def preorder(self, rt):
        if rt is None:
            return
        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    def postorder(self, rt):
        if rt is None:
            return
        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end=" ")

    # Count leaf nodes
    def count_leaf_nodes(self, rt):
        if rt is None:
            return 0
        if rt.left is None and rt.right is None:
            return 1
        return self.count_leaf_nodes(rt.left) + self.count_leaf_nodes(rt.right)


b1 = BST()
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

print("\nNumber of leaf nodes:", b1.count_leaf_nodes(b1.root))
