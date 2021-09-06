class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def valid_int(s):
            return True if len(s) == 1 or s[0] != '0' else False
        
        def valid_frac(s):
            return True if s[-1] != '0' else False
        
        def valid_set(s):
            result = set()
            if valid_int(s):
                result.add(s)
            for i in xrange(1, len(s)):
                if valid_int(s[:i]) and valid_frac(s[i:]):
                    result.add(s[:i]+'.'+s[i:])
            return result
        
        S = S[1:-1]
        result = set()
        for i in xrange(1, len(S)):
            x, y = valid_set(S[:i]), valid_set(S[i:])
            for xx in x:
                for yy in y:
                    result.add('('+xx+', '+yy+')')
        return list(result)