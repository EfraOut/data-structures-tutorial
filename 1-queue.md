# Queue
> **An Englishman, even if he is alone, forms an orderly queue of one**

 > George Mikes

Have you ever stood in line? Maybe the line for the self-checkout at Walmart was long. Or maybe you've been camping outside the store for hours waiting for midnight and get those Black Friday Discounts.

If you have experienced anything similar to that, congratulations! You have an empirical understanding of what a queue is. And if you haven't experienced anything like that, even more congratulations!

## What is a queue?
A queue is an orderly list, but we only care about the beginning and the end. Let's bring back the example of standing in line to illustrate a queue. Suppose that you are done doing your groceries shopping, and now is time to checkout. You see the big line of people waiting to checkout as well. What do you do? 

Hopefully you decide to go to the end of the line (cutting line is not allowed!). When are you going to get your turn to checkout? When everyone in front of you has checked out.

This system is commonly referred to as First In, First Out, or FIFO for short. And that is how a queue works. Every data registered in a queue will be added to the end of the list, and the list will be emptied based on the added order.

## Queues in Python
Now, let's get more technical.

In a queue, the first element is called the **front** and the last element is called the **back.** Adding to a queue is called **enqueue** (you entering the line) and removing from a queue is called **dequeue** (other people checking out while you wait).

A queue is not included in Python, but we can build one using the built-in `list`:

```python
class Simple_Queue:
    """
    A simple queue built on Python.
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
```

Please take special notice on how the dequeue method works. First, is going to check that the queue is not empty, just to prevent errors. Then, if the list is not empty, it will get the first value of the queue and store it in a variable, then it will delete that value from the queue, and finally it will return the value.

It is important to notice the deleting part. Without that part, the program will always dequeue the same value, and the queue will never get empty.
## Big O Notation
Operator        | Performance
----------------|------------
enqueue(value)  | O(1)
dequeue()       | O(n)*
size()          | O(1)
empty()         | O(1)

\* If the queue is implemented on an array, it will be O(n). If it is implemented on a linked list (more on that later) it will be O(1). 
## Example
The [following example](/code/queue_example.py) has the implementation of the other two operators: `size()` and `empty()`, and a simple program that will help you understand the concepts in action.
## Try it out!
Your family has been having issues with the assigned chores! You and your siblings agreed to take turns on washing the dishes. When any of you has done it, they will do it again once everyone has done it as well.
Follow [this link](/code/family_chores.py) to implement a queue so you can keep track of who's next. After you are done, compare your answer to the [sample solution](/code/family_chores_solution.py). This is just a solution, it doesn't mean it is the only way of solving it.

[Go back to Welcome Page](0-welcome.md)