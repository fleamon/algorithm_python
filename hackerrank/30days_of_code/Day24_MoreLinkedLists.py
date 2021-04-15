# -*- encoding: utf-8

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
        p = Node(data)
        if head==None:
            head=p
        elif head.next==None:
            head.next=p
        else:
            start=head
            while(start.next!=None):
                 start=start.next
            start.next=p
        return head
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        res = []
        queue = []
        if head:
            queue.insert(0, head)
            while queue:
                head = queue.pop()
                res.append(head.data)
                if head.next:
                    queue.insert(0, head.next)
        answer = []
        answer.append(str(res[0]))
        for i in range(1, len(res)):
            if res[i] != res[i - 1]:
                answer.append(str(res[i]))
        print " ".join(answer)

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);


"""
6
1
2
2
3
3
4


1 2 3 4
"""
