from collections import deque

class Solution:
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        queue = deque()
        queue.append((0, 1, 0))
        visited = set()
        
        while queue:
            x, v, steps = queue.popleft()
            if x == target:
                return steps
            if abs(x - target) > 2 * target:
                continue
            forward = (x+v, 2*v)
            if forward not in visited:
                visited.add(forward)
                queue.append((x+v, 2*v, steps+1))
            reverse_v = -1 if v > 0 else 1
            reverse = (x, reverse_v)
            if reverse not in visited:
                visited.add(reverse)
                queue.append((x, reverse_v, steps+1))
        
        return float('inf')
            
            
        
        
        