import heapq
import math

class Solution:
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """

        start = 0
        speed = 1
        pq = [(0, 0, start, speed)]
        cost = {(start, speed): 0}

        while pq:
            # f = estimated distance (priority)
            # g = actual distance travelled (depth)
            f, g, pos, speed = heapq.heappop(pq)
            if pos == target: return g
            if f > cost[(pos, speed)]: continue

            npos = pos + speed
            nspeed = speed * 2
            if target != npos:
                nt = math.ceil(math.log2(abs(target - npos) / abs(speed))) - 1
            else:
                nt = 0
            if nt < 0: nt = 0
            ncost = g + 1 + nt
            if ncost < cost.get((npos, nspeed), float('inf')):
                cost[(npos, nspeed)] = ncost
                heapq.heappush(pq, (ncost, g + 1, npos, nspeed))

            npos = pos
            if speed > 0:
                nspeed = -1
            else:
                nspeed = 1
            if target != npos:
                nt = math.ceil(math.log2(abs(target - npos) / abs(speed))) - 1
            else:
                nt = 0
            if nt < 0: nt = 0
            ncost = g + 1 + nt
            if ncost < cost.get((npos, nspeed), float('inf')):
                cost[(npos, nspeed)] = ncost
                heapq.heappush(pq, (ncost, g + 1, npos, nspeed))