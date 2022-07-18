# Tree
> **I am Groot!**

> Groot

![Climbing a tree](/pictures/Tree.jpg)

Some people enjoy working on their family history. It can be fun to trace back where you come from, and where your parents come from, and where their parents come from...

People find it useful to see all that information on a family tree. In the family tree, the individual place themselves as a dot, and two "branches" come out of it. Each of the branches then connects to a dot, which represent their parents. Each of the parents then also has two branches coming out, which represents their parents. And the process continues.

## What is a tree?
A tree not only gives us life through oxygen, but it is also a very good tool for sorting and finding.

Remember when we talked about Linked Lists? If not, [review that information first](/2-linked-list.md) before moving on. Trust me, it will help you understand things better. Basically, a tree is a Linked List, but each node connects to more than one other node.

The first node is called the **root**. If the next node is not connected to another node, it is called a **leaf.** If it does have a node, it is called a **parent.**
Each node connected to a **parent** is a **child.** Any node to the left or right to the parent is a **subtree**

![Tree diagram](/pictures/Tree_diagram.png)

As you can see on the diagram above, a tree follows the following rules:
* The root determines where the new node will go.
* If it is bigger than the root, it will go to the right.
* If it is smaller than the root, it will to the right.
* All of these rules apply to the subtrees.
## Recursion
Try searching "recursion" on Google and see what happens!

A definition of recursion is *a function that calls itself.* Maybe it does that because it doesn't have friends. In either way, recursion can be very powerful, as you will see in the following examples:

* [Example of recursion.](#tree)

* A tree uses recursion in his methods, as you will be able to see on the [implementation below.](#tree-in-python)

* The Francois numbers is a number sequence similar to Fibonacci. The first digit starts as 2, the second digit starts as 1, and the third (and subsequential digits) are the adding of the last two digits.
The following Python code shows how to use a tail recursion to find the *n* Francois number:

```python
def françois(n):
    """
    The Lucas series has the same recursive relationship as the
    Fibonacci sequence, where each term is the sum of the two
    previous terms, but with different starting values.
    The starting values are 2 and 1, instead of 0 and 1 as
    Fibonacci.
    """
    def go(n, first_digit, second_digit):
        """ 
        Tail recursion call.
        Parameters:
        n: The nth digit to be searched for.
        first_digit: The second-to-last digit that was found.
        second_digit: The last digit that was found.
        return:
        After all the recursion is done, it returns the second_digit
        """

        # Base cases.
        if n <= 0:
            return "Invalid number. Please enter a positive integer"
        if n == 2:
            return second_digit
        if n == 1:
            return first_digit

        # Recursive call.
        else:
            return go((n-1), second_digit, first_digit + second_digit)

    return go(n, 2, 1)
```
## Tree in Python
Here is an implementation of a Binary Search Tree, or BST for short:

```python
class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        elif data > node.data:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)

    def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        """
        This function will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        if node is not None:
            if node.data == data:
                return True
            else:
                if node.data < data:
                    return self._contains(data, node.right)
                else:
                    return self._contains(data, node.left)

    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a 
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.  
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
        """
        Perform a formward traversal (in order traversal) starting from 
        the root of the BST.  This function is called when a the 
        reversed function is called and is frequently used with a for
        loop.

        for value in reversed(my_bst):
            print(value)

        """        
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):
        """
        Does a backwards traversal (reverse in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the right
        side (thus getting the larger numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the left side (thus getting the smaller numbers last).

        This function is intended to be called the first time by 
        the __reversed__ function.        
        """
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    def get_height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        
        If the tree is empty, then return 0.  Otherwise, call 
        _get_height on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    def _get_height(self, node, height=1):
        """
        Determine the height of the BST.  The height of a sub-tree
        (represented by 'node') is 1 plus the height of either the
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        """ 
        if node.right is None and node.left is None:
            return height
        else:
            if node.right is None and node.left is not None:
                return self._get_height(node.left, height + 1)
            elif node.right is not None and node.left is None:
                return self._get_height(node.right, height + 1)
            else:
                return max(self._get_height(node.left, height + 1), self._get_height(node.right, height + 1))
```

## Big O Notation
Operator          | Performance
------------------|------------
insert(value)     | O(log n)
remove(value)     | O(log n)
contains(value)   | O(log n)
traverse_forward  | O(n)
traverse_reverse  | O(n)
height(node)      | O(n)
size()            | O(1)
empty()           | O(1)

Every time you traverse to either left or right, you are leaving behind the other halve. That is why the performance of a tree is O(log n)!
## Example
Lorem ipsum dolor sit amet.
## Try it out!
Lorem ipsum dolor sit amet.

[Go back to Welcome Page](0-welcome)