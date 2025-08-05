class BST:
    
    def __init__(self, root_node_value ):
        self.node_value = root_node_value
        self.leftChild = None
        self.rightChild = None
        
    def insert( self, currentNode, new_value ):
        
        # If Tree is not created, Root is None
        # if self.rootNode == None:
        #     self.rootNode = TreeNode( new_value )
        # else:
        #     # Value < Current Node's value - Left Side
            if new_value < currentNode.node_value:
                # If there are no Child Nodes just create the Node to the Left of currentNode
                if currentNode.leftChild == None:
                    currentNode.leftChild = BST( new_value ) 
                # Else keep Traversing the Tree Recursively
                else:
                    self.insert( currentNode.leftChild, new_value )
            else:
                # Value > Current Node's value - Right Side
                # If there are no Child Nodes just create the Node to the Right of currentNode
                if currentNode.rightChild == None:
                    currentNode.rightChild = BST( new_value ) 
                # Else keep Traversing the Tree Recursively
                else:
                    self.insert( currentNode.rightChild, new_value )

    def print_TreeNode( self, currentNode ):
        print( '\t \t ', currentNode.node_value )
        if currentNode.leftChild != None or currentNode.rightChild != None:
            print( '\n ', currentNode.leftChild, ' \t\t\t ', currentNode.rightChild )
            
    def inorder_traversal( self, currentNode ):
        if currentNode != None:
            self.inorder_traversal(currentNode.leftChild)
            print(currentNode.node_value, end=' -> ')
            self.inorder_traversal(currentNode.rightChild)

    def preorder_traversal( self, currentNode ):
        if currentNode != None:
            print(currentNode.node_value, end=' -> ')
            self.preorder_traversal(currentNode.leftChild)
            self.preorder_traversal(currentNode.rightChild)

    def postorder_traversal( self, currentNode ):
        if currentNode != None:
            self.postorder_traversal(currentNode.leftChild)
            self.postorder_traversal(currentNode.rightChild)
            print(currentNode.node_value, end=' -> ')
            

rootNode = BST( 10 )
rootNode.insert( rootNode, 7 )
rootNode.insert( rootNode, 12 )
rootNode.insert( rootNode, 18 )
rootNode.insert( rootNode, 3 )

print("\n Inorder Traversal of the Binary Search Tree:")
rootNode.inorder_traversal( rootNode )

print("\n PreOrder Traversal of the Binary Search Tree:")
rootNode.preorder_traversal( rootNode )

print("\n Postorder Traversal of the Binary Search Tree:")
rootNode.postorder_traversal( rootNode )