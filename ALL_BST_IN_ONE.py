
# Binary Search Tree (BST)

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert Node
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

    # Inorder Traversal
    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)

    # Preorder Traversal
    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    # Postorder Traversal
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")

    # Level Order Traversal
    def level_order(self, rt):
        if rt is None:
            print("BST is empty")
            return

        arr = []
        cnt = 0
        arr.append(rt)

        while cnt < len(arr):
            temp = arr[cnt]
            cnt += 1

            print(temp.data, end=" ")

            if temp.left:
                arr.append(temp.left)

            if temp.right:
                arr.append(temp.right)

    # Level Wise Display
    def level_wise_display(self, rt):
        if rt is None:
            print("BST is empty")
            return

        arr = []
        cnt = 0
        level = 0
        arr.append(rt)

        while cnt < len(arr):
            node_count = len(arr) - cnt

            print("\nLevel NO:", level, end=" ")

            for i in range(node_count):
                temp = arr[cnt]
                cnt += 1

                print(temp.data, end=" ")

                if temp.left:
                    arr.append(temp.left)

                if temp.right:
                    arr.append(temp.right)

            level += 1

    # Search Node
    def search(self, rt, key):
        if rt is None:
            return False

        if rt.data == key:
            return True

        elif key < rt.data:
            return self.search(rt.left, key)

        else:
            return self.search(rt.right, key)

    # Find Minimum Value
    def find_min(self, rt):
        if rt is None:
            return None

        while rt.left is not None:
            rt = rt.left

        return rt.data

    # Find Maximum Value
    def find_max(self, rt):
        if rt is None:
            return None

        while rt.right is not None:
            rt = rt.right

        return rt.data

    # Delete Node
    def delete(self, rt, key):
        if rt is None:
            return rt

        if key < rt.data:
            rt.left = self.delete(rt.left, key)

        elif key > rt.data:
            rt.right = self.delete(rt.right, key)

        else:
            if rt.left is None:
                return rt.right

            elif rt.right is None:
                return rt.left

            temp = rt.right

            while temp.left is not None:
                temp = temp.left

            rt.data = temp.data
            rt.right = self.delete(rt.right, temp.data)

        return rt

    # Count Total Nodes
    def count_nodes(self, rt):
        if rt is None:
            return 0

        else:
            return 1 + self.count_nodes(rt.left) + self.count_nodes(rt.right)

    # Count Leaf Nodes
    def count_leaf_nodes(self, rt):
        if rt is None:
            return 0

        if rt.left is None and rt.right is None:
            return 1

        return self.count_leaf_nodes(rt.left) + self.count_leaf_nodes(rt.right)

    # Count Left Leaf Nodes
    def left_leaf_nodes(self, rt):
        if rt is None:
            return 0

        cnt = 0

        if rt.left is not None:
            if rt.left.left is None and rt.left.right is None:
                cnt += 1
            else:
                cnt += self.left_leaf_nodes(rt.left)

        cnt += self.left_leaf_nodes(rt.right)

        return cnt

    # Count Right Leaf Nodes
    def right_leaf_nodes(self, rt):
        if rt is None:
            return 0

        cnt = 0

        if rt.right is not None:
            if rt.right.left is None and rt.right.right is None:
                cnt += 1
            else:
                cnt += self.right_leaf_nodes(rt.right)

        cnt += self.right_leaf_nodes(rt.left)

        return cnt

    # Count Child Nodes
    def count_child_nodes(self, rt):
        if rt is None:
            return 0

        cnt = 0

        if rt.left is not None or rt.right is not None:
            cnt += 1

        cnt += self.count_child_nodes(rt.left)
        cnt += self.count_child_nodes(rt.right)

        return cnt


# Object Calling Part

b1 = BST()

while True:

    print("\n\n----- BST MENU -----")
    print("1. Insert Node")
    print("2. Inorder Traversal")
    print("3. Preorder Traversal")
    print("4. Postorder Traversal")
    print("5. Level Order Traversal")
    print("6. Level Wise Display")
    print("7. Search Node")
    print("8. Delete Node")
    print("9. Count Total Nodes")
    print("10. Count Leaf Nodes")
    print("11. Count Left Leaf Nodes")
    print("12. Count Right Leaf Nodes")
    print("13. Count Child Nodes")
    print("14. Find Minimum Value")
    print("15. Find Maximum Value")
    print("16. Exit")

    ch = int(input("\nEnter your choice: "))

    if ch == 1:
        value = int(input("Enter the value of node: "))
        b1.insert(Node(value))
        print("Node inserted successfully")

    elif ch == 2:
        print("Inorder:")
        b1.inorder(b1.root)

    elif ch == 3:
        print("Preorder:")
        b1.preorder(b1.root)

    elif ch == 4:
        print("Postorder:")
        b1.postorder(b1.root)

    elif ch == 5:
        print("Level Order:")
        b1.level_order(b1.root)

    elif ch == 6:
        print("Level Wise Display:")
        b1.level_wise_display(b1.root)

    elif ch == 7:
        value = int(input("Enter the value to search: "))

        if b1.search(b1.root, value):
            print("Node found")
        else:
            print("Node not found")

    elif ch == 8:
        value = int(input("Enter the value to delete: "))

        if b1.search(b1.root, value):
            b1.root = b1.delete(b1.root, value)
            print("Node deleted successfully")
        else:
            print("Node not found")

    elif ch == 9:
        print("Total Nodes:", b1.count_nodes(b1.root))

    elif ch == 10:
        print("Total Leaf Nodes:", b1.count_leaf_nodes(b1.root))

    elif ch == 11:
        print("Left Leaf Nodes:", b1.left_leaf_nodes(b1.root))

    elif ch == 12:
        print("Right Leaf Nodes:", b1.right_leaf_nodes(b1.root))

    elif ch == 13:
        print("Child Nodes:", b1.count_child_nodes(b1.root))

    elif ch == 14:
        value = b1.find_min(b1.root)

        if value is None:
            print("BST is empty")
        else:
            print("Minimum Value:", value)

    elif ch == 15:
        value = b1.find_max(b1.root)

        if value is None:
            print("BST is empty")
        else:
            print("Maximum Value:", value)

    elif ch == 16:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")
