def preorder(node):
    preorder_result.append(node)
    left_node, right_node = tree[node]
    if left_node != '.':
        preorder(left_node)

    if right_node != '.':
        preorder(right_node)


def inorder(node):
    left_node, right_node = tree[node]
    if left_node != '.':
        inorder(left_node)

    inorder_result.append(node)

    if right_node != '.':
        inorder(right_node)


def postorder(node):
    left_node, right_node = tree[node]
    if left_node != '.':
        postorder(left_node)

    if right_node != '.':
        postorder(right_node)

    postorder_result.append(node)


import sys

input = sys.stdin.readline

n = int(input())
tree = {}
preorder_result = []
inorder_result = []
postorder_result = []

for i in range(n):
    parent, left, right = input().split()
    tree[parent] = (left, right)

preorder('A')
inorder('A')
postorder('A')

print(''.join(preorder_result))
print(''.join(inorder_result))
print(''.join(postorder_result))
