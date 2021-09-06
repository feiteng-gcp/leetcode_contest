class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """

        queue = [(0, 1)]
        hashMap = {(0, 1): 0}
        path = {}
        l = 0

        def getPath(x):
            while x in path:
                print x
                x = path[x]


        while l < len(queue):
            pos, spd = queue[l]
            l += 1
            newPos = pos + spd
            newSpd = spd * 2
            if newPos > 0 and abs(newPos) <= 10000 and newPos+newSpd >= 0 and (newPos, newSpd) not in hashMap:
                queue.append((newPos, newSpd))
                hashMap[(newPos, newSpd)] = hashMap[(pos, spd)] + 1
                # path[(newPos, newSpd)] = (pos, spd)
            if newPos == target:
                # getPath((newPos, newSpd))
                return hashMap[(newPos, newSpd)]
            newPos = pos
            if spd > 0:
                newSpd = -1
            else:
                newSpd = 1
            if (newPos, newSpd) not in hashMap:
                queue.append((newPos, newSpd))
                hashMap[(newPos, newSpd)] = hashMap[(pos, spd)] + 1
                # path[(newPos, newSpd)] = (pos, spd)

# print Solution().racecar(2)
