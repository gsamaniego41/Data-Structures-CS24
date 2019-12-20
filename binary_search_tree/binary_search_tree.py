from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # insert left if value is less than node
        if value < self.value:
            # if empty, create a new tree with its own value, left, and right properties
            if not self.left:
                self.left = BinarySearchTree(value)
            # else, keep going
            else:
                # self.left has its own left and right
                self.left.insert(value)
        # insert right if value is equal or greater than node
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        # Return True if the tree contains the value
        # False if it does not
        # if target == self.value, return it
        # go left or right based on smaller or bigger

        # base case
        if target == self.value:
            return True

        if target < self.value:
            if not self.left:
                # no child node
                return False
            else:
                # keep searching
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right
        # otherwise return self.value
        max = self.value

        while self:
            if self.value > max:
                max = self.value
            self = self.right
        return max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # keep iterating as long as current node has left and right
        if not self:
            return
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        # keep iterating
        cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # base case
        if node is not None:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # Make a stack
        queue = Queue()
        # put root in queue
        queue.enqueue(self)

        # while queue not empty
        while queue.len() > 0:
            # pop root out of stack
            current_node = queue.dequeue()
            # DO THE THING!!!!
            # print('cur', current_node.value)
            print(current_node.value)
            # if left : add left to stack
            if current_node.left:
                queue.enqueue(current_node.left)
            # if right : add left to stack
            if current_node.right:
                queue.enqueue(current_node.right)

        # print('---------')
        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal

    def dft_print(self, node):
        stack = Stack()
        stack.push(self)
        while stack.len() > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

        # STRETCH Goals -------------------------
        # Note: Research may be required

        # Print In-order recursive DFT
    def pre_order_dft(self, node):
        if node is not None:
            # "DO THE THING"
            print(node.value)
            # traverse left
            self.pre_order_dft(node.left)
            # traverse right
            self.pre_order_dft(node.right)

    # # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is not None:
            # traverse left
            self.post_order_dft(node.left)
            # traverse right
            self.post_order_dft(node.right)
            # finally, "DO THE THING"
            print(node.value)


""" 
bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

print(bst.bft_print(1)) 
"""
