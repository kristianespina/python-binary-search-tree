from random import randint #optional
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        if(value < self.value):
            if (self.left == None):
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif(value > self.value):
            if (self.right == None):
                self.right = Node(value)
            else:
                self.right.insert(value)
        else:
            self.value = value

    def convert_to_array(self, node, array):
        '''
        Uses Depth-First Search
        '''
        if node:
            array.append(node.value)
            self.convert_to_array(node.left, array)
            self.convert_to_array(node.right, array)
        return(array)


class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        if(self.root is None):
            self.root = Node(data)
        else:
            self.root.insert(data)

    def find(self,data):
        return self.find_node(self.root,data)
        
    def find_node(self, node, data):
        if node is None:
            return False
        elif data == node.value:
            return True
        elif data < node.value:
            return(self.find_node(node.left,data))
        else:
            return(self.find_node(node.right,data))

    def convert_to_array(self):
        return(self.root.convert_to_array(self.root,[]))
    def rearrange(self):
        '''
        Re-arrange the binary tree in such a way
        that the median is the root of the tree
        @return Binary Tree in DFS Array Form
        '''
        nodes = self.convert_to_array()
        nodes.sort()
        middle = len(nodes)//2
        self.root = Node(nodes.pop(middle))
        for element in nodes:
            self.root.insert(element)
        return(self.convert_to_array())

tree = BinaryTree()
for i in range(50):
    tree.insert(randint(0,100))
print(tree.convert_to_array())
print(tree.rearrange())
print(tree.find(55))