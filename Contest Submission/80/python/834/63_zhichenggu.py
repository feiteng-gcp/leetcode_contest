class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        
        
        def get_all_s(s):
            if len(s) < 0:
                return []
            if len(s) == 1:
                return [s]
            if s[0] == '0':
                if s[-1] != '0':
                    return [s[0] + '.' + s[1:]]
                else:
                    return []
            if s[-1] == '0':
                return [s]
            res = [s]
            for i in range(1, len(s)):
                res.append(s[:i] + '.' + s[i:])
            return res
        
        msg = S[1:-1]
        
        res = []
        for i in range(1, len(msg)):
            lst1 = get_all_s(msg[:i])
            lst2 = get_all_s(msg[i:])
            if lst1 and lst2:
                for n1 in lst1:
                    for n2 in lst2:
                        res.append('(' + n1 + ', ' + n2 + ')')
        return res