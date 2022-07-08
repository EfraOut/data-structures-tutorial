class LinkedList:
    """
    Implement the LinkedList data structure. The Node class below is an inner class.
    """
    class Node:
        '''
        Each node of the linked list will have data and links to the 
        previous and next node. 
        '''

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

    def insert(self, value):
        """
        Insert a new node to the linked list.
        """
        # Create the new node.
        new_node = LinkedList.Node(value)

        # If the list is empty, then point both head and tail
        # to the new node.
        if self.current is None:
            new_node.next = new_node.prev
            new_node.prev = new_node.next
            self.current = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.prev = self.current # Connect new node to current
            self.current.next = new_node # Connect previous node to new node
            new_node.next = self.current.prev # Connect new node back to current
            self.current.prev = new_node.next # Connect current back to new node
            self.current = new_node
        
    def __iter__(self):
        """
        Iterate forward through the Linked List
        """
        nodes = []
        curr = self.current  # Start at the beginning since this is a forward iteration.
        while curr is not None:
            if curr.data in nodes:
                return
            else:
                yield curr.data  # Provide (yield) each item to the user
                nodes.append(curr.data)
            curr = curr.next # Go forward in the linked list

    def __reversed__(self):
        """
        Iterate backward through the Linked List
        """
        yield "???"
    
uno_game = LinkedList()


done = False
while not done:
    player = input("Enter the name of the player (Enter 'done' when finished): ")
    if player.lower() == "done":
        done = True
    else:
        uno_game.insert(player)
        print(player, "has been added.")

print("The players are: ")
for node in uno_game:
    print(node, end=" || ")