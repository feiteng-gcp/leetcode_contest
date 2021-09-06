class Solution:
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target == 0:
            return 0
        visitedStates = {(0, 1)}
        states = [(0, 1)]
        step = 1
        while True:
            new_states = []
            for state in states:
                # least n st. 2^n >= |target|  [log_2 target] + 1
                # least k st. 2^k >= 2^n - |target|   []
                # least j st  2^j >= |target| - (2^n - 2^k)
                # A
                next_state = (state[0] + state[1], 2 * state[1])
                if next_state[0] == target:
                    return step
                if next_state not in visitedStates:
                    visitedStates.add(next_state)
                    if (target > 0 and next_state[0] > 0) or (target < 0 and next_state[0] < 0):
                        new_states.append(next_state)
                # R
                next_state = (state[0], -1 if state[1] > 0 else 1)
                if next_state not in visitedStates:
                    visitedStates.add(next_state)
                    new_states.append(next_state)
            states = new_states
            step += 1