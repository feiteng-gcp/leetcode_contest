# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        charSet = set(G)
        flag = False
        tmp = head
        res = 0
        while tmp:
            if tmp.val in charSet:
                if not flag:
                    flag = True
            else:
                if flag:
                    flag = False
                    res += 1
            tmp = tmp.next
        if flag:
            res += 1
        return res
        
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        