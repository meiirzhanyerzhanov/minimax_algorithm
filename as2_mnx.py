#Assignment 2
from as2_tree import Tree
class Result:
	def __init__(self, sol=[], val=-1000):
			self.solution = sol
			self.value = val
			
class MNX:
	def __init__(self, data_list):
		self.tree = Tree()	
		self.tree.init_tree(data_list)
		self.root = self.tree.root
		self.currentNode = None
		self.successors = []		
		return

	def terminalTest(self, node):
		assert node is not None
		return len(node.children) == 0

	def utilityChecking(self, node):
		assert node is not None
		return node

	def getChildren(self, node):
		assert node is not None
		return node.children

	def minimax(self):
		terminal_val = self.max_v(self.root)
		successors = self.getChildren(self.root)
		traversed=[] #example of solution_array
		res=Result()


#################  Return the solution here  #################
		res.value=terminal_val.value #you put the best terminal value for root node here
#################  Return the solution here  #################

		temp_node = terminal_val
		traversed2 = []
		while(temp_node.Name!=self.root.Name):
			traversed2.append(temp_node.Name)
			temp_node = temp_node.parent
		traversed2.append(self.root.Name)
		for i in reversed(traversed2):
			traversed.append(i)
		res.solution = traversed
		return res


	def max_v(self, node):
		if self.terminalTest(node):
			return self.utilityChecking(node)
		max_v = Result() #we use -1000 as the initial_maximum value
		max_v.value = -1000
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			temp_node = self.min_v(deeper_node)
			if(max_v.value<temp_node.value):
				max_v = temp_node

		return max_v

	def min_v(self, node):
		if self.terminalTest(node):
			return self.utilityChecking(node)
		min_v = Result()
		min_v.value = 1000 #we use 1000 as the initial_minimum value
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			temp_node = self.max_v(deeper_node)
			if(min_v.value>temp_node.value):
				min_v = temp_node
		return min_v