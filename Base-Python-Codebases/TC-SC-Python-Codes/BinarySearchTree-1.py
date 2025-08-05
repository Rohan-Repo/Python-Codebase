# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None

#     def insert(root, newValue):
#         if root is None:
#             root = BinaryTreeNode(newValue)
#             return root
#         if newValue < root.data:
#             root.leftChild = insert(root.leftChild, newValue)
#         else:
#             root.rightChild = insert(root.rightChild, newValue)
#         return root

#     def print_tree(self, level=0, label='.'):
#             print(' ' * (level*2) + label + ':', self.value)
#             if self.left:
#                 self.left.print_tree(level+1, '<')
#             if self.right:
#                 self.right.print_tree(level+1, '>')

# root = BinaryTreeNode(5)
# root.insert(2)
# root.insert(7)
# root.insert(1)
# root.insert(3)
# root.insert(6)
# root.insert(8)

# root.print_tree()

def insert(root, newValue):
    if root is None:
        return {'data': newValue, 'leftChild': None, 'rightChild': None}
    if newValue < root['data']:
        root['leftChild'] = insert(root['leftChild'], newValue)
    else:
        root['rightChild'] = insert(root['rightChild'], newValue)
    return root

def inorder_traversal(root):
    elements = []
    if root['leftChild']:
        elements += inorder_traversal(root['leftChild'])
    elements.append(root['data'])
    if root['rightChild']:
        elements += inorder_traversal(root['rightChild'])
    return elements

def print_tree(node, level=0, label='.'):
    print(' ' * (level*2) + label + ':', node['data'])
    if node['leftChild']:
        print_tree(node['leftChild'], level+1, '<')
    if node['rightChild']:
        print_tree(node['rightChild'], level+1, '>')

# Example usage:
root = None
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 7)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 6)
root = insert(root, 8)

print_tree(root)
