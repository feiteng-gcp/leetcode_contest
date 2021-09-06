class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        pS = S[1:-1]
        def allValid(s):
            # print s
            if len(s) > 1 and s[0] == '0' and s[-1] == '0':
                return []
            if len(s) == 1:
                return [s]
            if s[0] == '0':
                return ['0.{}'.format(s[1:])]
            if s[-1] == '0':
                return [s]
            r = [s]
            for i in xrange(1, len(s)):
                r.append('{}.{}'.format(s[:i], s[i:]))
            return r
            
        result = []
        for i in xrange(1, len(pS)):
            # print pS[:i], pS[i:]
            left = allValid(pS[:i])
            right = allValid(pS[i:])
            if not left or not right:
                continue
            for l in left:
                for r in right:
                    t = '({}, {})'.format(l, r)
                    result.append(t)
        return result
        