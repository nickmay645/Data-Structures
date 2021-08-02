from stack import *


if __name__ == "__main__":
    stack = create_stack()
    push(stack, str(1))
    push(stack, str(2))
    push(stack, str(3))
    push(stack, str(4))
    print("peek item: " + peek(stack))
    print("stack after peeking an element: " + str(stack))
    print("popped item: " + pop(stack))
    print("stack after popping an element: " + str(stack))
