import sys


def get_input():
    return sys.stdin.readline().rstrip()


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self):
        self.nodes = {}
        self.root = None

    def create_or_get_node(self, value):
        if value not in self.nodes:
            node = Node(value)
            self.nodes[value] = node
            if not self.root:
                self.root = node
            return node
        else:
            return self.nodes[value]

    def connect(self, parent_value, left_child_value, right_child_value):
        parent = self.create_or_get_node(parent_value)
        if left_child_value != ".":
            left_child = self.create_or_get_node(left_child_value)
            parent.left_child = left_child
        if right_child_value != ".":
            right_child = self.create_or_get_node(right_child_value)
            parent.right_child = right_child

        if not self.root:
            self.root = parent

    def traverse_pre(self, node):
        result = node.value
        if node.left_child:
            result += self.traverse_pre(node.left_child)
        if node.right_child:
            result += self.traverse_pre(node.right_child)

        return result

    def traverse_in(self, node):
        result = ""
        if node.left_child:
            result += self.traverse_in(node.left_child)
        result += node.value
        if node.right_child:
            result += self.traverse_in(node.right_child)

        return result

    def traverse_post(self, node):
        result = ""
        if node.left_child:
            result += self.traverse_post(node.left_child)
        if node.right_child:
            result += self.traverse_post(node.right_child)
        result += node.value

        return result


binaryTree = BinaryTree()
n = int(get_input())
for i in range(n):
    parent_value, left_child_value, right_child_value = get_input().split()
    binaryTree.connect(parent_value, left_child_value, right_child_value)

print(binaryTree.traverse_pre(binaryTree.root), end="")
print()
print(binaryTree.traverse_in(binaryTree.root), end="")
print()
print(binaryTree.traverse_post(binaryTree.root), end="")
