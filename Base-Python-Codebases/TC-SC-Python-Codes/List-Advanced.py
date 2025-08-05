# # Stack using Lists 
stack_of_books = []

# Push to the End of the Stack/List
def push( book_num ):
    stack_of_books.append( book_num )

# Pop the Top-most/Last Element from Stack/List
def pop():
    if stack_of_books:
        return stack_of_books.pop()
    else:
        print( 'Stack is Empty! ' )

# Display Stack
def display_stack():
    print( '\n Stack Contents: ', stack_of_books )
    print( '\n Stack Length: ', len(stack_of_books) )
    
# Push Elements to the Stack
for i in range(5):
    push( i )
    display_stack()

# Pop Elements from Stack
print( '\n Popped Element = ', pop() )
display_stack()

# Push to the Stack
push( 99 )
display_stack()

# Pop Elements from Stack
print( '\n Popped Element = ', pop() )
display_stack()

# Pop Elements from Stack
print( '\n Popped Element = ', pop() )
display_stack()

# Pop Elements from Stack
print( '\n Popped Element = ', pop() )
display_stack()


# Queue with List
person_queue = []

# Enqueue to the End of the Queue/List
def enqueue( person_num ):
    person_queue.append( person_num )

# dequeue the First Element from Queue/List
def dequeue():
    if person_queue:
        return person_queue.pop(0)
    else:
        print( 'Queue is Empty! ' )

# Display Stack
def display_queue():
    print( '\n Queue Contents: ', person_queue )
    print( '\n Queue Length: ', len(person_queue) )
    
# Enqueue Elements to the Queue
for i in range(5):
    enqueue( i )
    display_queue()

# Dequeue Elements from Queue
print( '\n Dequeued Element = ', dequeue() )
display_queue()

# Enqueue to the Queue
enqueue( 99 )
display_queue()

# Dequeue Elements from Queue
while( dequeue() ):
    print( '\n Dequeued Element = ', dequeue() )
    display_queue()