class Superset:
    """
    Implement the circular LinkedList data structure.
    The Node class below is an inner class.
    """
    class Node:
        """
        Each node of the linked list will have data and links to the 
        previous and next node.
        """
        def __init__(self, data):
            """ 
            Initialize the node to the data provided. Initially
            the links are unknown so they are set to None.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.current = None
        self.first = None

    def insert(self, value):
        """
        Insert a new node to the linked list.
        """
        # Create the new node.
        new_node = Superset.Node(value)

        # If the list is empty, then point both current and first
        # to the new node.
        if self.current is None:
            new_node.next = new_node.prev
            new_node.prev = new_node.next
            self.current = new_node
            self.first = new_node
        # If the list is not empty, then connect first and current
        # to each other.
        else:
            new_node.prev = self.current # Connect new node to current
            self.current.next = new_node # Connect previous node to new node
            new_node.next = self.first.prev # Connect new node to first
            self.first.prev = new_node.next # Connect first to new node
            self.current = new_node # Change current to new node

    def __iter__(self):
        """
        Iterate forward through the Linked List
        """
        nodes = []
        curr = self.first  # Start from the first node.
        while curr != None:
            if curr.data in nodes:
                return
            else:
                yield curr.data  # Provide (yield) each item to the user
                nodes.append(curr.data)
            curr = curr.next # Go forward in the linked list

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output


# First, change the Node, so it can store, the name of the exercise
# and the number of repetitions.
# Hint: You also need to change the __iter__ yield the added values.

# Initialize an instance of Superset.

# Store on a variable the number of sets to perform.

# Using the insert() method, add the exercises to perform.

# Display the exercises to perform and the number of sets.