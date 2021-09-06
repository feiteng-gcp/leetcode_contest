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
        this = head
        before = None
        next_dict = dict()
        before_dict = dict()
        max_num = None
        while this:
            max_num = max(max_num, this.val)
            if this.next:
                next_dict[this.val] = this.next.val
            if before:
                before_dict[this.val] = before.val
            before, this = this, this.next
        k = US(max_num + 1)
        for num in G:
            k.tree[num] = num
            before = before_dict.get(num)
            after = next_dict.get(num)
            if before is not None and k.tree[before] is not None:
                k.merge(before, num)
            if after is not None and k.tree[after] is not None:
                k.merge(after, num)
        res = set()
        for i in k.tree:
            if i is not None:
                res.add(k.find_parent(i))
        return len(res)
        
        
class US(object):
    def __init__(self, length):
        self.tree = [None] * length
        self.height = [0] * length
        
    def find_parent(self, index):
        if self.tree[index] != index:
            self.tree[index] = self.find_parent(self.tree[index])
        return self.tree[index]
    
    def merge(self, a, b):
        a = self.find_parent(a)
        b = self.find_parent(b)
        if self.height[a] > self.height[b]:
            self.height[a] += 1
            self.tree[b] = a
        else:
            self.height[b] += 1
            self.tree[a] = b
        
            
        