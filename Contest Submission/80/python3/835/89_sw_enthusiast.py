# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        G = set(G)
        item = head
        sol, started = 0, False
        while item != None:
            if item.val in G:
                if not started:
                    started = True
            else:
                if started:
                    sol += 1
                    started = False
            item = item.next
        if started:
            sol += 1
        return sol