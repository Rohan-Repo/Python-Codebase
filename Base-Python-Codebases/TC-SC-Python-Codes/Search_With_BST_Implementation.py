print( '\t' * 10 ,'Linear Search, Binary Search and Binary Search Tree Implementation!' )
# Start with a list of 100 random integers from 1 to 1000
# 1. Write a simple program that 
# Asks a user to enter a number.
# Determines whether or not the number is in the list.
# Counts each time the number is compared to a number already in the list (it could be the first thing you look at or it might not be in the list after checking all 100 entries).

import random

# Generate a list of 100 random integers from 1 to 1000
num_list = []

for _ in range(100):
    num_list.append( random.randint(1, 1000) )

print( '\n Num List : ', num_list )

# Enter a number to Search 
num_to_search = int( input("\n Enter a number to Search in our List and BST: ") )

print( '\n Linear Search Implementation:' )

def linear_search ( num_to_search, number_list ):
    comparisons = 0

    for num in number_list:
        comparisons += 1

        # Keep Traversing the List until we find the number
        if num == num_to_search:
            return True, comparisons

    # If number not found then return False along with comparison count
    return False, comparisons

# Search for the user's number in the list
found, comparison_count = linear_search ( num_to_search, num_list )

# Display the result
if found:
    print( "\n\t The number",  num_to_search, " is Found in the List." )
else:
    print( "\n\t The number",  num_to_search, " was Not Found in the List." )

print( "\n\t Linear-Search - Number of comparisons made: ",  comparison_count )

print( '\n Binary Search Implementation:' )

def binary_search ( num_to_find, numList ):
    comparisons = 0

    start = 0
    end = len( numList ) - 1

    for i in range( len(numList) ):
        comparisons += 1

        # Since we need a Decimal Value and not a Float one, we do Floor Division
        mid_point = (start + end) // 2

        # print( '\n\t start : ', start, ' , end : ', end, ' , mid_point : ', mid_point  )
        # print( '\t Internal List : ', numList[ start: end+1 ] )
        
        # Is the Number present at Mid-Point?
        if numList[ mid_point ] == num_to_find:
            return True, comparisons
            break

        #  Start cannot be > End - Stopping Condition so return False along with comparison count
        elif start > end:
            return False, comparisons
            break
        
        # If num_to_find > mid-point , Change the Start point 
        elif num_to_find > numList[ mid_point ]:
            start = mid_point + 1
        
        # If num_to_find < mid-point , Change the End point
        elif num_to_find < numList[ mid_point ]:
            end = mid_point - 1

# Search for the user's number in the list
isFound, comparison_count = binary_search ( num_to_search, num_list )

# Display the result
if isFound:
    print( "\n\t The number",  num_to_search, " is Found in the List." )
else:
    print( "\n\t The number",  num_to_search, " was Not Found in the List." )

print( "\n\t Binary-Search - Number of comparisons made: ",  comparison_count )

#  Now, build the Binary Search Tree to sort the list
# For each number, create a node with the number and left- and right-links set NULL.
# Add the number to the tree 
# The first time, it becomes the root.
# After that, decide on left-or right-link. If the link is NULL, assign it to this new node, otherwise, decide left- or right-linked node and repeat.
# Now, ask the user to enter a number and follow the links until you find a node that matches the number or there is a NULL link. (Do not add the user number.)
# Count the number of comparisons. It could be the root node, it could match a subsequent node, or you might run out of choices, indicating it is not in the list.

print( '\n Binary Search Tree Implementation:' )

import random

# Create the TreeNode class with a Value and LeftChild and RightChild nodes
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, new_node):

    # If Tree is not created, Root is None
    if root is None:
        return new_node

    # if Value < Current Node's value - Add it on the Left Side of the tree
    if new_node.value < root.value:
        root.left = insert_node(root.left, new_node)
    
    # else if Value > Current Node's value - Add it on the Right Side of the tree
    elif new_node.value > root.value:
        root.right = insert_node(root.right, new_node)

    return root

def search_number_in_tree(root, num_to_search ):
    comparisons = 0

    # Here we check if the Tree first exists or not
    while root is not None:
        comparisons += 1

        # If the value we are searching for is at the Root Node then Great No need to check others
        if num_to_search == root.value:
            return True, comparisons
        
        # Since it's a BST, if the number to search < TreeNode value then check in the left side of the tree
        elif num_to_search < root.value:
            root = root.left

        # Since it's a BST, if the number to search > TreeNode value then check in the right side of the tree
        else:
            root = root.right

    # If number not found then return False along with comparison count
    return False, comparisons

# Use the Same Numbers from Above List


# Build the Binary Search Tree
bst_root = None
for number in num_list:
    new_node = TreeNode(number)
    bst_root = insert_node(bst_root, new_node)

# Search for the same user's number in the BST
found, comparison_count = search_number_in_tree( bst_root, num_to_search )

# Display the result
if found:
    print( "\n\t The number",  num_to_search, " is Found in the tree." )
else:
    print( "\n\t The number",  num_to_search, " was Not Found in the tree." )

print( "\n\t Binary Search Tree - Number of comparisons made: ",  comparison_count )