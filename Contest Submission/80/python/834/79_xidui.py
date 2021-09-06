class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = []
        def possibleStr(s):
            ret = [s]
            if not s:
                return []
            if len(s) > 1 and s[0] == s[-1] == '0':
                return []
            if s[-1] == '0' or len(s) == 1:
                return [s]
            if s[0] == '0':
                return [s[0] + '.' + s[1:]]
            for i in range(1, len(s)):
                ret.append("{0}.{1}".format(s[:i], s[i:]))
            return ret
                
        S = S[1:-1]
        for i in range(len(S)):
            left = possibleStr(S[:i])
            right = possibleStr(S[i:])
            for l in left:
                for r in right:
                    ans.append("({0}, {1})".format(l, r))
        return ans
        