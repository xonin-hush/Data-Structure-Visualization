# import graphviz

# dot = graphviz.Digraph('round-table', comment='The Round Table')
# dot.node('A', 'King Arthur')  
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')
# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', constraint='false')
# print(dot.source)  

class Node:
    def __init__(self, root):
        self.root = root
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if data < self.root:
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)

    def search(self, val):
        if val == self.root:
            return str(val) + " is found in the BST"
        elif val < self.root:
            if self.leftChild:
                return self.leftChild.search(val)
            else:
                return str(val) + " is not found in the BST"
        else:
            if self.rightChild:
                return self.rightChild.search(val)
            else:
                return str(val) + " is not found in the BST"

    def draw_tree(self, level=0, prefix=""):
        if self.rightChild:
            self.rightChild.draw_tree(level + 1, prefix + "    ")
        print(" " * 4 * level + prefix + str(self.root))
        if self.leftChild:
            self.leftChild.draw_tree(level + 1, prefix + "    ")

    def print_inorder(self):
        if self.leftChild:
            self.leftChild.print_inorder()
        print(self.root, end=" ")
        if self.rightChild:
            self.rightChild.print_inorder()

    def delete(self, val):
        # Step 1: Find the node to be deleted
        if val < self.root:
            # If the value is less than the current node's value,
            # recursively call delete on the left subtree
            if self.leftChild:
                self.leftChild = self.leftChild.delete(val)
        elif val > self.root:
            # If the value is greater than the current node's value,
            # recursively call delete on the right subtree
            if self.rightChild:
                self.rightChild = self.rightChild.delete(val)
        else:
            # Step 2: Perform deletion based on different cases
           
            # Case 1: Deleting a leaf node (A node with no children)
            if not self.leftChild:
                return self.rightChild  # Returning the right child or None if it's also None
            elif not self.rightChild:
                return self.leftChild  # Returning the left child
           
            # Case 2: Deleting a node with one child
            else:
                # Find the minimum value in the right subtree
                min_right = self.rightChild
                while min_right.leftChild:
                    min_right = min_right.leftChild
                # Swap values between the current node and the minimum value node
                self.root = min_right.root
                # Recursively delete the minimum value node from the right subtree
                self.rightChild = self.rightChild.delete(min_right.root)
        return self  # Return the modified node or subtree root

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(39)
root.insert(7)
root.insert(37)
root.insert(11)

print("Inorder Traversal:")
root.print_inorder()
print("\n")

print("Searching the values:")
print(root.search(7))
print(root.search(14))

print("\nBinary Search Tree (Vertical):")
# root.draw_tree()

print("Deleting node with value 10:(2 children)")
root.delete(10)
print("Binary Search Tree after deletion:")
# root.draw_tree()
print("\n")

print("Deleting node with value 11:(1 child)")
root.delete(11)
print("Binary Search Tree after deletion:")
# root.draw_tree()
print("\n")

print("Deleting node with value 7:(No children)")
root.delete(27)
root.draw_tree()