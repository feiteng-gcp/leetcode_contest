from collections import deque

class Solution(object):
    
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        q = deque([(0, 1)])
        vis = set([(0, 1)])
        dst = 0
        while True:
            new_q = deque([])
            for pos, sp in q:
                npos, nsp = pos+sp, sp*2
                if npos == target:
                    return dst+1
                if abs(npos) < 2*target and (npos, nsp) not in vis:
                    new_q.appendleft((npos, nsp))
                    vis.add((npos, nsp))
                npos, nsp = pos, -1
                if sp <= 0:
                    nsp = 1
                if (npos, nsp) not in vis:
                    new_q.appendleft((npos, nsp))
                    vis.add((npos, nsp))
            q = new_q
            dst += 1
        
        
        