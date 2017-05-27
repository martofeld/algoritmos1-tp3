from Stack import Stack

class LinkedList():
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

	def pop(self, index = None):
		if i < 0 or i > self.len:
			raise IndexError("Invalid index for list")

		self.len -= 1

		if index == None:
			index = self.len

		if index == 0:
			return_value = self.first.value
			self.first = self.first.next
			return return_value

		previous = None
		current = self.first
		for i in range(index):
			previous = current
			current = current.next
		previous.next = current.next
		return current.dato

	def __iter__(self):
		return _LinkedListIterator(self.first)


class _LinkedListIterator():
	"""docstring for _LinkedListIterator"""
	def __init__(self, start_value):
		self.current = start_value
		self.previous = Stack()

	def next(self):
		self.previous.push(self.current)
		if not self.current.next:
			raise StopIteration

		return_value = self.current.value
		self.current = self.current.next
		return return_value

	def __next__(self):
		return self.next()

	def previous(self):
		if self.previous.is_empty():
			raise StopIteration

		self.current = self.previous.pop()
		return self.current.value

	def has_next(self):
		return self.current.next != None



class _Node():
	"""docstring for _Node"""
	def __init__(self, value):
		self.value = value
		self.next = None
		