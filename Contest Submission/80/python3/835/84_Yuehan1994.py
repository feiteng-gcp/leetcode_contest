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
        import collections
        G = set(G)
        neighbors = collections.defaultdict(set)
        node = head
        next = head.next
        while next:
            neighbors[node.val].add(next.val)
            neighbors[next.val].add(node.val)
            node = next
            next = node.next
        res = 0
        while G:
            visited = set()
            q = [G.pop()]
            visited.add(q[0])
            i = 0
            while i < len(q):
                cur = q[i]
                i += 1
                for j in neighbors[cur]:
                    if j not in visited and j in G:
                        visited.add(j)
                        G.remove(j)
                        q.append(j)
            res += 1
        return res