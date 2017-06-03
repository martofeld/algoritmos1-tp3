class Stack():
    """ADT impl for the Stack"""

    def __init__(self):
        self.container = []

    def pop(self):
        """Returns and removes the top of the stack"""
        if self.is_empty():
            return None

        return self.container.pop()

    def push(self, value):
        """Adds a new value to the top of the stack"""
        self.container.append(value)

    def is_empty(self):
        """Returns if the stack is empty"""
        return len(self.container) == 0

    def peek(self):
        """Returns but does not remove the top of the stack"""
        if self.is_empty():
            return None

        return self.container[-1]
