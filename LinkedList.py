from Stack import Stack


class LinkedList:
    """docstring for LinkedList"""

    def __init__(self):
        self.first = None
        self.last = None
        self.len = 0

    def push(self, value):
        new = _Node(value)
        self.len += 1

        if not self.first or not self.last:
            self.first = self.last = new
            return;

        self.last.next = new
        self.last = new

    def insert(self, value, index=None):
        if index is None or index == self.len:
            push(value)

        if index < 0 or index > self.len:
            raise IndexError

        new = _Node(value)
        self.len += 1
        if index == 0:
            new.next = self.first
            self.first = new
            return

        previous = self.first
        for i in range(1, index):
            previous = previous.next

        new.next = previous.next
        previous.next = new

    def replace(self, new_value, index):
        if index < 0 or index > self.len:
            raise IndexError

        if index == 0:
            self.first.value = new_value
            return

        previous = self.first
        for i in range(1, index + 1):
            previous = previous.next

        previous.value = new_value

    def pop(self, index=None):
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

    def get(self, index=None):
        if index is None:
            index = self.len - 1

        if index < 0 or index > self.len:
            raise IndexError("Invalid index for list")

        current = self.first
        for i in range(index):
            current = current.next

        return current.value

    def get_range(self, start=None, end=None):
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
    """docstring for _LinkedListIterator"""

    def __init__(self, start_value):
        self.current = start_value
        self.previous_stack = Stack()

    def next(self):
        if not self.current:
            raise StopIteration

        self.previous_stack.push(self.current)

        return_value = self.current.value
        self.current = self.current.next
        return return_value

    def __next__(self):
        return self.next()

    def previous(self):
        if self.previous_stack.is_empty():
            raise StopIteration

        self.current = self.previous_stack.pop()
        return self.current.value

    def has_next(self):
        return self.current.next != None

    def has_previous(self):
        return not self.previous_stack.is_empty()

    def get_current(self):
        return self.current.value

    def insert(self, value):
        self.insert_previous(value)
        self.previous()

    def insert_next(self, value):
        next_node = self.current.next
        new_node = _Node(value)
        self.current.next = new_node
        new_node.next = next_node

    def insert_previous(self, value):
        new_node = _Node(value)
        self.previous_stack.peek().next = new_node
        new_node.next = self.current
        self.previous_stack.push(new_node)


class _Node:
    """docstring for _Node"""

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
