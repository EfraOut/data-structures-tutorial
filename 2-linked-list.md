# Linked List
> **[Quote goes here]**

> Author

Imagine it is Easter Time, and you are a kid. Your parents are excited to set you loose in the search of the easter eggs they hid throughout the garden. To help you on your quest, you received a map showing one of the eggs. As soon as you get to the X, you find an egg! When you open the egg, you find another map, showing the location of another egg. Finding that egg reveals another map that leads to another map. After following these clues for what felt like ages, you found the final map. It leads back to your house, where your mom has baked your favorite cake.

Was it worth it to go through all those clues, just for that cake? After all the cake is a lie. It's up to you to decide.

## Throwing a barbecue (and understanding memory)
Let's talk about memory, and we will use the garden previously mentioned as an analogy.

Suppose you are throwing a barbecue, and you are expecting 15 friends to come over (hopefully you have that many friends for this example to work), so you set up 15 chairs. They all arrive right on time, but to your surprise, they invited more people to the barbecue! You have plenty of meat, so that's not a problem. But the chairs! You didn't set up enough of them. Luckily you have more stored on the basement, so you take the ones you need and put them in the garden, allowing every guest to have somewhere to sit.

Let's discuss now the technical part of a Linked List.
## What is a Linked List?
When adding elements (variables) to memory, it takes space. If want to put a chair on the garden, it will take a specific place. Since the garden has a limited space (it can't expand after you start), you can't store infinite chairs.

A Linked List differs from an array because the memory is used when needed, and not together when declared. The amount of chairs varied because there were more guests than expected. But how can the Linked List know which elements are inside, if they are all over the place? **Pointers.** The easter eggs had a map that showed you where the next clue, or egg, was.

So every element (called **nodes**) has a value, and a pointer that tells you where the next node is and where the previous node is.

## Linked List on Python
It is possible to have a Linked List on Python, **but** we will have to do it ourselves. There is no built-in Linked List (Note: There is a Linked List implementation that can be imported. Just add `from collections import deque`), because there is no notion of pointers on Python. The `list()` function is actually an array (very misleading name, if you ask me).
,
The elements that we need to create a Linked List are the following:

1. Node: The individual element that creates a list there are three characteristics from a node:
* Data: The value contained within the node.
* Next: The pointer that tell us where the next node is.
* Prev: The pointer that tell us where the previous node is.
2. Head: The first node from the Linked List. The Prev pointer points to `None`
3. Tail: The last node from the Linked List. The Next pointer points to `None`

Here is an implementation:

```python
class LinkedList:
    """
    Implement the LinkedList data structure. The Node class below is an inner class.
    """
    class Node:
        
        Each node of the linked list will have data and links to the 
        previous and next node. 
        

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
        self.head = None
        self.tail = None

    def insert_head(self, value):
        """
        Insert a new node at the front (i.e. the head) of the
        linked list.
        """

        # Create the new node.
        new_node = LinkedList.Node(value)  

        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node

    def insert_tail(self, value):
        """
        Insert a new node at the back (i.e. the tail) of the 
        linked list.
        """
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.tail will be
        # affected.
        else:
            new_node.prev = self.tail # Connect new node to the next tail
            self.tail.next = new_node # Connect the previous head to the new node
            self.tail = new_node      # Update the tail to point to the new node

    def remove_head(self):
        """ 
        Remove the first node (i.e. the head) of the linked list.
        """
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node

    def remove_tail(self):
        """
        Remove the last node (i.e. the tail) of the linked list.
        """
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.tail is not None:
            self.tail.prev.next = None  # Disconnect the second node from the first node
            self.tail = self.tail.prev  # Update the head to point to the second node

    def insert_after(self, value, new_value):
        """
        Insert 'new_value' after the first occurrence of 'value' in
        the linked list.
        """
        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        curr = self.head
        while curr is not None:
            if curr.data == value:
                # If the location of 'value' is at the end of the list,
                # then we can call insert_tail to add 'new_value'
                if curr == self.tail:
                    self.insert_tail(new_value)
                # For any other location of 'value', need to create a 
                # new node and reconnect the links to insert.
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr       # Connect new node to the node containing 'value'
                    new_node.next = curr.next  # Connect new node to the node after 'value'
                    curr.next.prev = new_node  # Connect node after 'value' to the new node
                    curr.next = new_node       # Connect the node containing 'value' to the new node
                return # We can exit the function after we insert
            curr = curr.next # Go to the next node to search for 'value'

    def remove(self, value):
        """
        Remove the first node that contains 'value'.
        """
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr.next == None:
                    self.remove_tail()
                    return
                elif curr.prev == None:
                    self.remove_head()
                    return
                else:
                    curr.next.prev = curr.prev
                    curr.prev.next = curr.next
                    return
            curr = curr.next

    def replace(self, old_value, new_value):
        """
        Search for all instances of 'old_value' and replace the value 
        to 'new_value'.
        """
        curr = self.head  # Start at the beginning since this is a forward iteration.
        while curr is not None:
            if curr.data == old_value:
                curr.data = new_value
            curr = curr.next
        
    def __iter__(self):
        """
        Iterate forward through the Linked List
        """
        curr = self.head  # Start at the beginning since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    def __reversed__(self):
        """
        Iterate backward through the Linked List
        """
        curr = self.tail  # Start at the end since this is a backward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.prev # Go backward in the linked list

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output
```

## Big O Notation
Operator            | Performance
--------------------|------------
insert_head(value)  | O(1)
insert_tail()       | O(1)
insert(i, value)    | O(n)
remove_head()       | O(1)
remove_tail(index)  | O(1)
remove(i)           | O(n)
size()              | O(1)
empty()             | O(1)
## Example
Lorem ipsum dolor sit amet.

## Try it out!
You like to exercise, and you want to try doing a superset. A superset is performing *n* amount of repetitions on the same exercises. You can implement a circular linked list to do that. [Here is the code](/code/superset.py) for you to create your workout. A [sample solution](/code/superset_example.py) is provided for you to compare your answer. Have fun, and remember: It's bulking season!