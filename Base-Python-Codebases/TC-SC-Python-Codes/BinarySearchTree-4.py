# Using Python,
# Start with a list of 100 random integers from 1 to 1000
# 1. Write a simple program that 
# Asks a user to enter a number.
# Determines whether or not the number is in the list.
# Counts each time the number is compared to a number already in the list (it could be the first thing you look at or it might not be in the list after checking all 100 entries).

# import random

# # Generate a list of 100 random integers from 1 to 1000
# random_numbers = [random.randint(1, 1000) for _ in range(100)]

# def search_number(user_number, number_list):
#     comparisons = 0

#     for number in number_list:
#         comparisons += 1
#         if number == user_number:
#             return True, comparisons

#     return False, comparisons

# # Ask the user to enter a number
# user_input = int(input("Enter a number: "))

# # Search for the user's number in the list
# found, comparisons_made = search_number(user_input, random_numbers)

# # Display the result
# if found:
#     print(f"The number {user_input} is in the list.")
# else:
#     print(f"The number {user_input} is not in the list.")

# print(f"Number of comparisons made: {comparisons_made}")

# For the Above Program,
#  Now, build the Binary Search Tree to sort the list
# For each number, create a node with the number and left- and right-links set NULL.
# Add the number to the tree 
# The first time, it becomes the root.
# After that, decide on left-or right-link. If the link is NULL, assign it to this new node, otherwise, decide left- or right-linked node and repeat.
# Now, ask the user to enter a number and follow the links until you find a node that matches the number or there is a NULL link. (Do not add the user number.)
# Count the number of comparisons. It could be the root node, it could match a subsequent node, or you might run out of choices, indicating it is not in the list.

import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, new_node):
    if root is None:
        return new_node

    if new_node.value < root.value:
        root.left = insert_node(root.left, new_node)
    elif new_node.value > root.value:
        root.right = insert_node(root.right, new_node)

    return root

def search_number_in_tree(root, user_number):
    comparisons = 0

    while root is not None:
        comparisons += 1
        if user_number == root.value:
            return True, comparisons
        elif user_number < root.value:
            root = root.left
        else:
            root = root.right

    return False, comparisons

# Generate a list of 100 random integers from 1 to 1000
random_numbers = []

for _ in range(100):
    random_numbers.append( random.randint(1, 1000) )

print( 'Num List : ', random_numbers )

# Build the Binary Search Tree
bst_root = None
for number in random_numbers:
    new_node = TreeNode(number)
    bst_root = insert_node(bst_root, new_node)

# Ask the user to enter a number
user_input = int(input("Enter a number: "))

# Search for the user's number in the BST
found, comparisons_made = search_number_in_tree(bst_root, user_input)

# Display the result
if found:
    print(f"The number {user_input} is in the tree.")
else:
    print(f"The number {user_input} is not in the tree.")

print(f"Number of comparisons made: {comparisons_made}")

