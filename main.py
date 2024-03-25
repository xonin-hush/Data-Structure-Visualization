import graphviz

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def visualize_binary_tree(root):
    dot = graphviz.Digraph()
    dot.node(str(root.key))

    def add_nodes_edges(node):
        if node.left:
            dot.node(str(node.left.key))
            dot.edge(str(node.key), str(node.left.key))
            add_nodes_edges(node.left)
        if node.right:
            dot.node(str(node.right.key))
            dot.edge(str(node.key), str(node.right.key))
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    dot.render('binary_tree', view=True, format='png')
#delete
def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = get_min_value(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def get_min_value(root):
    while root.left is not None:
        root = root.left
    return root
#end of delete

# Example usage:
root = None
keys = [5, 3, 7, 2, 4, 6, 8,1,9]
for key in keys:
    root = insert(root, key)

visualize_binary_tree(root)