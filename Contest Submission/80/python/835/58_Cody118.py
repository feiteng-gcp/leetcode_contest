# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """

        def merge(x, y):
            xx = getFather(x)
            yy = getFather(y)

            father[xx] = yy

        def getFather(x):
            if father[x] == x:
                return x

            father[x] = getFather(father[x])
            return father[x]

        vec = {}
        for v in G:
            vec[v] = True

        edge = {}
        n = 0
        while head:
            n += 1
            if head.val in vec:
                if head.next and head.next.val in vec:
                    edge[head.val] = head.next.val
            head = head.next

        father = [i for i in xrange(n)]

        for i in G:
            if i in edge:
                merge(i, edge[i])

        s = set()
        for i in G:
            s.add(getFather(i))
            
        return len(s)

# head = ListNode(0)
# head.next = ListNode(1)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(3)
# head.next.next.next.next = ListNode(4)
#
# print Solution().numComponents(head, [0, 3, 1, 4])
