class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def valid(s):
            if s.startswith("-"):
                s = s[1:]
            if s == "":
                return False
            if s == "0":
                return True
            if s.startswith(".") or s.endswith("."):
                return False
            if s.startswith("0") and not s.startswith("0."):
                return False
            if "." in s and s.endswith("0"):
                return False
            return True
        
        def gen(str):
            l = []
            if valid(str):
                l.append(str)
            for i in range(1, len(str)):
                str2 = str[:i] + "." + str[i:]
                if valid(str2):
                    l.append(str2)
            return l
            
        S = S[1:-1]
        r = []
        for i in range(1, len(S)):
            g1 = gen(S[:i])
            g2 = gen(S[i:])
            for j in g1:
                for k in g2:
                    r.append("(" + j + ", " + k + ")")
        return r