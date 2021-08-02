# Stack implementation in python

# Creating a stack
def create_stack():
    stack = []
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0


# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if check_empty(stack):
        return "stack is empty"

    return stack.pop()


def peek(stack):
    if check_empty(stack):
        return "stack is empty"

    return stack[len(stack)-1]


"""
Stack Time Complexity
For the array-based implementation of a stack, the push and pop operations take constant time, i.e. O(1).
"""
