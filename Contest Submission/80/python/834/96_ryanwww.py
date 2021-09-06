class Solution(object):
    def ambiguousCoordinates(self, S):
        S = S[1:-1]
        res = []
        def util(s):
            res = []
            if len(s) == 1:
                return [s]
            if s[0] != '0':
                res.append(s)
            if s[-1] == '0':
                return res
            if s[0] == '0':
                res.append(s[0]+'.'+s[1:])
                return res
            else:
                for i in range(1, len(s)):
                    res.append(s[0:i] + '.' + s[i:])
            return res

        for i in range(1, len(S)):
            front = util(S[0: i])
            back = util(S[i: ])
            if front and back:
                for i in front:
                    for j in back:
                        tmp = '('
                        tmp += i
                        tmp += ', '
                        tmp += j
                        tmp += ')'
                        res.append(tmp)
        return res
        """
        :type S: str
        :rtype: List[str]
        """
        