
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        q = [(0, 1, 0)]
        vis = set([(0,1)])
        guard = 0
        guard2 = target * 2
        while q:
            p, v, t = q.pop(0)
            # A
            for p1, v1 in [(p+v, v*2),
                    (p, (-1 if v>0 else 1))]:
                if p1 == target:
                    return t+1
                if p1 < guard:
                    continue
                if p1 > guard2:
                    continue
                if (p1,v1) not in vis:
                    vis.add((p1,v1))
                    q.append((p1, v1, t+1))
        return -1
