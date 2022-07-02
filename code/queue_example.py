"""
As you go through this example, make sure you read through
the comments and the code. It is important you understand
what we are talking about.

There is code you need to uncomment. They have been marked
with a number. As you encounter one, here's what I want you
to do:

1. Try to guess what that code of line will do. Be as specific
as possible.
2. Uncomment the line(s)
3. Run the program and compare your answer with the outcome.

Make sure you comprehend the code you just uncommented before
moving on.
"""

class Queue:
    """
    An orderly array in a FIFO system.
    """

    def __init__(self):
        """
        Initialize the empty queue using a Python List.
        """
        self.queue = []

    def enqueue(self, value):
        """
        Enqueue the value provided into the queue
        """
        self.queue.append(value)

    def dequeue(self):
        """
        Dequeue the next value and return it
        """
        if len(self.queue) <= 0:
            raise IndexError()
        value = self.queue[0]
        del self.queue[0]
        return value
    
    def is_empty(self):
        """
        Check to see if the queue is empty.
        """
        return len(self.queue) == 0
    
    def display(self):
        """
        Displays the values of the queue.
        """
        if len(self.queue) <= 0:
            print("There are no elements in the queue")
        else:
            print("The elements in the queue are:")
            for element in self.queue:
                print(element)

    def __len__(self):
        """
        This function will be called when using the
        len() function. 
        """
        return len(self.queue)



# Initialize a queue.
queue = Queue()

# Adding elements to the queue. This is going
# to be a queue of numbers
queue.enqueue(5)
queue.enqueue(1)
queue.enqueue(8)
queue.enqueue(9)

# Can you guess the order of the elements in the queue?
# queue.display() # 1

# Dequeuing two elements from the queue.
queue.dequeue()
queue.dequeue()

# Which elements will stay in the queue?
# queue.display() # 2

# Checking the length will tell us the number of
# elements.
# print("Elements in the queue:", len(queue)) # 3

# When we check for is_empty(), the program
# will return a boolean
# print("Is the queue empty?", queue.is_empty()) # 4