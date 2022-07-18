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
        def __init__(self, exercise_name, reps):
            """ 
            Initialize the node to the data provided. Initially
            the links are unknown so they are set to None.
            """
            self.exercise_name = exercise_name # Data added.
            self.reps = reps # Data added.
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.current = None
        self.first = None

    def insert(self, exercise_name, reps):
        """
        Insert a new node to the linked list.
        """
        # Create the new node.
        new_node = Superset.Node(exercise_name, reps)

        # If the list is empty, then point both head and tail
        # to the new node.
        if self.current is None:
            new_node.next = new_node.prev
            new_node.prev = new_node.next
            self.current = new_node
            self.first = new_node
        # If the list is not empty, then only self.head will be
        # affected.
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
        curr = self.first  # Start from current node. Since it is circular, it doesn't matter
        while curr != None:
            if id(curr) in nodes:
                return
            else:
                yield curr.exercise_name  # Provide (yield) each item to the user
                yield curr.reps  # Provide (yield) each item to the user
                nodes.append(id(curr))
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

# Initialize an instance of Superset.
superset = Superset()
# Store on a variable the number of sets to perform.
num_sets = int(input("Enter the number of sets: "))
# Using the insert() method, add the exercises to perform.
superset.insert("Pushup", 10)
superset.insert("Alternating Hammer Curl", 15)
superset.insert("Tricep Dip", 15)
superset.insert("Elbow Plank", 15)
# Display the exercises to perform and the number of sets.
print("You need to perform the following exercises", superset, "a total of", num_sets)