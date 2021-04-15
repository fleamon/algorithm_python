# -*- encoding: utf-8

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        queue = []
        if root:
            queue.insert(0, root)
            while queue:
                root = queue.pop()
                print root.data,
                if root.left:
                    queue.insert(0, root.left)
                if root.right:
                    queue.insert(0, root.right)

T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

"""
6
3
5
4
7
2
1


3 2 5 1 4 7
"""
