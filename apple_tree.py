class Node:
	def __init__(self, value, left=None, right=None, red=False):
		self.value = value
		self.left = left
		self.right = right
		self.red = red

	@staticmethod
	def red(node):
		return node and node.red

	def rotate_left(self):
		if not Node.red(self.left) and Node.red(self.right):
			child = self.right
			self.right, child.left = child.left, self
			self.red, child.red = True, self.red
			return child
		else:
			return self

	def rotate_right(self):
		if Node.red(self.left) and Node.red(self.left.left):
			child = self.left
			self.left, child.right = child.right, self
			self.red, child.red = True, self.red
			return child
		else:
			return self

	def flip_colors(self):
		if Node.red(self.left) and Node.red(self.right):
			self.red, self.left.red, self.right.red = True, False, False



def insert(node, value, root=True):
	if not node:
		return Node(value, red=not root)

	# # insert value
	# if value == node.value:
	# 	pass
	elif value <= node.value:
		node.left = insert(node.left, value, root=False)
	else:
		node.right = insert(node.right, value, root=False)

	# update tree w.r.t invariants
	node = node.rotate_left()
	node = node.rotate_right()
	node.flip_colors()

	# keep root black
	if root:
		node.red = False

	return node