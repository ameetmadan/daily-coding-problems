# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The following test should pass:
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def deserialize(self, s):
        if s == '#':
            return None
        else:
            node = Node(s)
            node.left = self.deserialize(s[1])
            node.right = self.deserialize(s[2])
            return node
    def serialize(self, node):
        if node is None:
            return '#'
        else:
            return str(node.val) + self.serialize(node.left) + self.serialize(node.right)

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert node.deserialize(node.serialize(node)).left.left.val == 'left.left'