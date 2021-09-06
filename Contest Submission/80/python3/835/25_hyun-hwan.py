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
        G = set(G)
        cur = head
        while cur != None:
          if not cur.val in G: cur.val = None
          cur = cur.next
        
        ret = 0
        num = 0
        
        cur = head
        while cur != None:
          if cur.val == None:
            if num > 0: 
              ret += 1
            num = 0
          else:
            num += 1
          cur = cur.next
        if num > 0:
          ret += 1
        return ret
                