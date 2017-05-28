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

	def insert(self, value, index = None):
		if index == None or index == self.len:
			push(value)
		if index < 0:
			raise IndexError

		new = _Node(value)
		self.len += 1
		if index == 0:
			new.next = self.first
			self.first = new
			return

		previous = self.first
		for i in range(1, index + 1):
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
		return current.value

	def __iter__(self):
		return _LinkedListIterator(self.first)

	def __len__(self):
		return self.len


class _LinkedListIterator():
	"""docstring for _LinkedListIterator"""
	def __init__(self, start_value):
		self.current = start_value
		self.previous = Stack()

	def next(self):
		if not self.current:
			raise StopIteration
		
		self.previous.push(self.current)

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
		