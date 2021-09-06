# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        st = set(G)
        t = head
        a = []
        i = -1
        while (t):
            i += 1
            if t.val in st:
                a.append(i)
            t = t.next
        a.sort()
        # print(a)
        if len(a) == 0:
            return 0
        ans = 1
        for i in range(1, len(a)):
            if a[i] != a[i-1]+1:
                ans += 1
        return ans