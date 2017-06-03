from LinkedList import LinkedList

def test_push():
	l_list = LinkedList()
	l_list.push(1)
	l_list.push(2)
	l_list.push(3)
	assert 3 == len(l_list)
	for i in range(1, 4):
		assert i == l_list.pop(0)

def test_get_range_empty():
	l_list = LinkedList()
	l_list.push(1)
	l_list.push(2)
	l_list.push(3)
	l_list.push(4)
	l_list.push(5)
	l_list.push(6)
	l_list.push(7)
	l_list.push(8)
	l_list.push(9)
	l_list.push(10)
	l_range = l_list.get_range()
	assert 10 == len(l_range)

	for i in range(10, 0, -1):
		assert i == l_range.pop()

def test_get_range_indexed():
	l_list = LinkedList()
	l_list.push(1)
	l_list.push(2)
	l_list.push(3)
	l_list.push(4)
	l_list.push(5)
	l_list.push(6)
	l_list.push(7)
	l_list.push(8)
	l_list.push(9)
	l_list.push(10)
	l_range = l_list.get_range(3, 8)
	assert 5 == len(l_range)

	for i in range(8, 3, -1):
		assert i == l_range.pop()

test_push()
test_get_range_indexed()
test_get_range_empty()

print("SUCCESFUL")