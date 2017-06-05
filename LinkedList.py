from Stack import Stack


class LinkedList:
    """class for the LinkedList ADT"""

    def __init__(self):
        """Creates a new instance of the LinkedList"""
        self.first = None
        self.last = None
        self.len = 0

    def push(self, value):
        """Adds a value to the end of the list"""
        new = _Node(value)
        self.len += 1

        if not self.first or not self.last:
            self.first = self.last = new
            return

        self.last.next = new
        self.last = new

    def pop(self, index=None):
        """Removes and returns the last value of the given index, by default the last value"""
        if index is None:
            index = self.len - 1

        if index < 0 or index > self.len:
            raise IndexError("Invalid index for list")

        self.len -= 1

        if index == 0:
            return_value = self.first.value
            self.first = self.first.next
            return return_value

        previous = self.first
        current = self.first.next
        for i in range(1, index):
            previous = current
            current = current.next
        previous.next = current.next
        return current.value

    def get_range(self, start=None, end=None):
        """Return a new list that is composed by the values of this one between start and end"""
        if start is None or start < 0:
            start = 0
        if end is None or end > self.len - 1:
            end = self.len

        current = self.first
        for i in range(start):
            current = current.next

        selected_range = LinkedList()
        for i in range(end - start):
            selected_range.push(current.value)
            current = current.next

        return selected_range

    def __iter__(self):
        return _LinkedListIterator(self.first)

    def __len__(self):
        return self.len

    def __str__(self):
        str_list = []
        for node in self:
            str_list.append(node)

        return str(str_list)


class _LinkedListIterator:
    """Iterator for the LinkedList"""

    def __init__(self, start_value):
        """Creates a new iterator"""
        self.current = start_value
        self.previous_stack = Stack()

    def next(self):
        """Moves the iterator to the next position and returns the value of the current one"""
        if not self.current:
            raise StopIteration

        self.previous_stack.push(self.current)

        return_value = self.current.value
        self.current = self.current.next
        return return_value

    def __next__(self):
        return self.next()

    def previous(self):
        """Moves the iterator to the previous position and returns the value of the current one"""
        if self.previous_stack.is_empty():
            raise StopIteration

        return_value = self.current.value
        self.current = self.previous_stack.pop()
        return return_value

    def has_next(self):
        """Checks if the iterator has a next value"""
        return self.current.next != None

    def has_previous(self):
        """Checks if the iterator has a previous value"""
        return not self.previous_stack.is_empty()

    def get_current(self):
        """Return the current value of the iterator"""
        return self.current.value

    def insert(self, value):
        """Insert a value in the current position"""
        self.insert_previous(value)
        self.previous()

    def insert_next(self, value):
        """Insert a value in the next position"""
        next_node = self.current.next
        new_node = _Node(value)
        self.current.next = new_node
        new_node.next = next_node

    def insert_previous(self, value):
        """Insert a value in the previous position"""
        new_node = _Node(value)
        self.previous_stack.peek().next = new_node
        new_node.next = self.current
        self.previous_stack.push(new_node)


class _Node:
    """a simple Node class for the LinkedList"""

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
