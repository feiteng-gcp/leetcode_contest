# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        s=set(G)
        p=head
        cnt=0
        while p:
            if p.val in s:
                cnt+=1
                while p and p.val in s:
                    p=p.next
            else:
                p=p.next
        return cnt