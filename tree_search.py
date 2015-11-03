class Node(object):
    def __init__(self, value):
        self.children = []
        self.value = value

    def add_child(self, node):
        self.children.append(node)

def dfs(root, value):
    if not value or not root:
        return None

    if root.value == value:
        return root

    for child in root.children:
        node = dfs(child, value)
        if node:
            return node

    return None
