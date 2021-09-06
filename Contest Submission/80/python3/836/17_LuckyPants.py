class Solution:
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target==0:
            return 0
        
        q = [(0, 1)]
        visited = set((0, 1))
        cnt = 0
        while q:
            # print(q)
            new_q = []
            cnt += 1
            for pos, sp in q:
                p1, s1 = pos+sp, sp*2
                if p1==target:
                    # print(len(visited))
                    # print(len(q))
                    return cnt
                p2, s2 = pos, -1 if sp>0 else 1
                if (p1, s1) not in visited:
                    if s1==1 or s1==-1:
                        visited.add((p1, s1))
                    new_q.append((p1, s1))
                if (p2, s2) not in visited:
                    visited.add((p2, s2))
                    if s1==1 or s1==-1:
                        visited.add((p1, s1))
                    new_q.append((p2, s2))
            q = new_q
        return -1
        
        