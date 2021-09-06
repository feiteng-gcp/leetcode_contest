
from collections import defaultdict


class Solution:
    def racecar(self, target):
        if target == 0:
            return 0

        rounds = 0
        pos_ref = defaultdict(set)
        stage = [(0, 1)]

        while True:
            next_stage = []
            while stage:
                pos, speed = stage.pop(0)
                if pos > 10000 or pos < -10000:
                    continue
                # A
                npos = pos + speed
                nspeed = speed * 2

                if npos == target:
                    return rounds + 1
                else:
                    if nspeed not in pos_ref[npos]:
                        pos_ref[npos].add(nspeed)
                        next_stage.append((npos, nspeed))

                # R
                npos = pos
                nspeed = -1 if speed > 0 else 1
                if nspeed not in pos_ref[npos]:
                    pos_ref[npos].add(nspeed)
                    next_stage.append((npos, nspeed))
            stage = next_stage
            rounds += 1
        