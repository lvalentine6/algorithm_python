import sys

sys.setrecursionlimit(100000)


class node:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y
        self.parent = None
        self.left = None
        self.right = None


def _insert(parent, child):
    if parent.x > child.x:
        if parent.left == None:
            parent.left = child
            child.parent = parent
        else:
            _insert(parent.left, child)
    else:
        if parent.right == None:
            parent.right = child
            child.parent = parent
        else:
            _insert(parent.right, child)


def pre_order(node):
    if node == None:
        return

    answer[0].append(node.num)
    pre_order(node.left)
    pre_order(node.right)


def post_order(node):
    if node == None:
        return

    post_order(node.left)
    post_order(node.right)
    answer[1].append(node.num)


def solution(nodeinfo):
    global answer
    answer = [[], []]

    for i, n in enumerate(nodeinfo):
        n.insert(0, i + 1)

    nodeinfo.sort(key=lambda x: (-x[2], x[1]))
    root = node(nodeinfo[0][0], nodeinfo[0][1], nodeinfo[0][2])

    for i in range(1, len(nodeinfo)):
        _insert(root, node(nodeinfo[i][0], nodeinfo[i][1], nodeinfo[i][2]))

    pre_order(root)
    post_order(root)

    return answer
