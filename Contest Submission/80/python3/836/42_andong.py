class Solution:
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        insts = {'': (0, 1)} # inst -> (pos, speed)
        cnt = 0
        while True:
            new_insts = {}
            cnt += 1
            for inst in insts:
                dist = target - insts[inst][0]
                cur_speed = insts[inst][1]
                # if (cur_speed >0 and dist > 0) or (cur_speed <0 and dist<0):
                    # A
                new_inst = inst + 'A'
                pos = insts[inst][0] + insts[inst][1]
                if pos == target:
                    return cnt
                speed = insts[inst][1]*2
                new_insts[new_inst] = (pos, speed)
                # R
                if (cur_speed >0 and dist < 0) or (cur_speed <0 and dist>0) or (cur_speed > 0 and cur_speed > dist) or (cur_speed < 0 and cur_speed < dist):
                    new_inst = inst + 'R'
                    pos = insts[inst][0]
                    speed = -1 if insts[inst][1] > 0 else 1
                    new_insts[new_inst] = (pos, speed)
            insts = new_insts    
            
