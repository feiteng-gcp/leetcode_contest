class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        position = 0
        speed = 1
        this_layer = [(position, speed)]
        res = 0
        while True:
            next_layer = set()
            for p, s in this_layer:
                if p == target:
                    return res
                if p > target and s > 16:
                    next_layer.add((p, -1))
                    continue
                if p < target and s < -16:
                    next_layer.add((p, 1))
                    continue
                next_layer.add((p, -1 if s > 0 else 1))
                next_layer.add((p + s, s * 2))
            this_layer = next_layer
            res += 1
        return -1