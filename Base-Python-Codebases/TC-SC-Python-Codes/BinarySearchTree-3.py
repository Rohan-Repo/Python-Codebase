# import random

# # Generate a list of 100 random integers between 1 and 1000
# random_list = [random.randint(1, 1000) for i in range(100)]

# # Ask the user to enter a number
# number = int(input("Enter a number: "))

# # Determine whether or not the number is in the list
# found = False
# count = 0
# for i in range(len(random_list)):
    # count += 1
    # if random_list[i] == number:
        # found = True
        # break

# # Print the result
# if found:
    # print(f"The number {number} was found in the list after {count} comparisons.")
# else:
    # print(f"The number {number} was not found in the list after {count} comparisons.")
    
import random

# Define the TreeNode class
class TreeNode:
    def __init__(self, node_value):
        self.node_value = node_value
        self.leftChild = None
        self.rightChild = None

    def print_TreeNode(self):
        print('\t \t ', self.node_value)
        print('\n ', self.leftChild, ' \t\t\t ', self.rightChild)

# Define the BST class
class BST:
    
    def __init__(self):
        self.rootNode = None

    def insert(self, currentNode, new_value):
        
        # If the tree is not created, the root is None
        if self.rootNode == None:
            self.rootNode = TreeNode(new_value)
        else:
            # Value < Current Node's value - Left Side
            if new_value < currentNode.node_value:
                # If there are no child nodes, just create the node to the left of currentNode
                if currentNode.leftChild == None:
                    currentNode.leftChild = TreeNode(new_value) 
                # Else keep traversing the tree recursively
                else:
                    self.insert(currentNode.leftChild, new_value)
            else:
                # Value > Current Node's value - Right Side
                # If there are no child nodes, just create the node to the right of currentNode
                if currentNode.rightChild == None:
                    currentNode.rightChild = TreeNode(new_value) 
                # Else keep traversing the tree recursively
                else:
                    self.insert(currentNode.rightChild, new_value)

    def search(self, currentNode, search_value, count):
        # If the current node is None, the search value is not in the tree
        if currentNode == None:
            return count, False
        
        # If the search value is equal to the current node's value, we have found the node
        if search_value == currentNode.node_value:
            return count, True
        
        # If the search value is less than the current node's value, search the left subtree
        if search_value < currentNode.node_value:
            count += 1
            return self.search(currentNode.leftChild, search_value, count)
        
        # If the search value is greater than the current node's value, search the right subtree
        if search_value > currentNode.node_value:
            count += 1
            return self.search(currentNode.rightChild, search_value, count)

# Generate a list of 100 random integers between 1 and 1000
random_list = [random.randint(1, 1000) for i in range(100)]

print( 'List : ', random_list )

# Build the binary search tree
bst = BST()
for i in range(len(random_list)):
    bst.insert(bst.rootNode, random_list[i])

# Ask the user to enter a number
number = int(input("Enter a number: "))

# Search for the number in the tree
count, found = bst.search(bst.rootNode, number, 1)

# Print the result
if found:
    print(f"The number {number} was found in the tree after {count} comparisons.")
else:
    print(f"The number {number} was not found in the tree after {count} comparisons.")

