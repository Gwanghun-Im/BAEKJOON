# 5639번 : 이진 검색 트리

import sys
sys.setrecursionlimit(10**5)

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def pre_order(node):
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)
    print(node.data)


def tree_insert(p, num):
    if p.data > num:
        if p.left :
            return tree_insert(p.left, num)
        p.left = Node(num)
    else:
        if p.right :
            return tree_insert(p.right, num)
        p.right = Node(num)

tree = Node(int(input()))
nums = []

while True:
    try:
        nums.append(int(input()))
    except:
        break

for i in nums:
    p = tree
    tree_insert(p, i)

pre_order(tree)
