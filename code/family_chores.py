"""
There are some queues called circular queues. After an element
is dequeued from the queue, it will go back to the queue. It is
the circle of life.

Help your siblings keep their assignments with the following queue.
"""

class Family_Chores:
    """
    An orderly array in a FIFO system.
    """
    def __init__(self):
        """
        Initialize the empty queue using a Python List.
        """
        self.queue = []

    def add_member(self, value):
        """
        Enqueue the value provided into the queue
        """
        self.queue.append(value)

    def select_member(self):
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
        return "???"
    
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
        return "???"

family = Family_Chores()

# Add every member of your family to the queue.

# Display who is the next person to wash the dishes.
# Also, don't forget to add them back, because everyone needs
# to stay in the queue!

# There is a way to enqueue the person again on the queue
# once it gets dequeue. Can you figure out how to do it?
# Hint: You only need to add one line of code!

# If you paid attention to the example code, you know how to
# implement the __len__() and is_empty() methods.
# Try to remember, and test your result with the following code.

# print(len(family))
# print("Is everyone still in the queue?", family.is_empty())