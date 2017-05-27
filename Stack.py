class Stack():
	"""docstring for Stack"""
	def __init__(self):
		self.container = []

	def pop(self):
		if self.is_empty():
			return None
			
		return self.container.pop()

	def push(self, value):
		self.container.append(value)

	def is_empty(self):
		return len(self.container) == 0

	def peek(self):
		if self.is_empty():
			return None

		return self.container[-1]