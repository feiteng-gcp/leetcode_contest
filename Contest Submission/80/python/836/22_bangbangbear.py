class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        states, step = [(0, 1)], 1
        visited = set()
        while True:
            new_state = set()
            for state in states:
                if state not in visited:
                    visited.add(state)
                    new_state.add((state[0], -1 if state[1] > 0 else 1))
                    newloc = state[0] + state[1]
                    if newloc == target:
                        return step
                    if newloc < target * 3 and newloc > -target:
                        new_state.add((newloc, state[1] * 2))
            states = new_state
            step += 1
        return -1


            