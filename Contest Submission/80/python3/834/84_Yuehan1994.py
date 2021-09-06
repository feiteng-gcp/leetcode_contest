class Solution:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def check(s):
            if '.' not in s:
                if s == '0':
                    return True
                if s[0] == '0':
                    return False
                return True
            nums = s.split('.')
            return check(nums[0]) and nums[1][-1] != '0'

        def helper(s):
            res = []
            if check(s):
                res.append(s)
            for i in range(1, len(s), 1):
                if check(s[:i] + '.' + s[i:]):
                    res.append(s[:i] + '.' + s[i:])
            return res

        res = []
        for i in range(2, len(S)-1, 1):
            temp1 = helper(S[1:i])
            temp2 = helper(S[i:len(S)-1])
            for n1 in temp1:
                for n2 in temp2:
                    res.append('(' + n1 + ', ' + n2 + ')')

        return res