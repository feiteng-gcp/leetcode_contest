class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def possibleS(s):
            l = len(s)
            if l == 0: return []
            if l == 1: return [s]
            if s[0] == '0':
                ret = []
            else:
                ret = [s]
            for i in range(1,l):
                t = s[:i] + '.' + s[i:]
                if t[-1] == '0' or t[0] == '0' and t[1] != '.':
                    continue
                ret += [t]
            return ret
        S = S[1:-1]
        l = len(S)
        ans = []
        for i in range(1,l):
            pre = possibleS(S[:i])
            post = possibleS(S[i:])
            if pre and post:
                #print 'pre', pre
                ans += [ "(" + x + ", " + y + ")" for x in pre for y in post ]
        return ans