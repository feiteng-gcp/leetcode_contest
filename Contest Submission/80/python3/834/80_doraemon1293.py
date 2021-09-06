class Solution:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def foo(a):
            res=[]
            for x in range(1,len(a)+1):
                x1=a[:x]
                x2=a[x:]
                if (x1[0]!="0" or x1=="0") and (x2=="" or x2[-1]!="0"):
                    if x2:
                        res.append(x1+"."+x2)
                    else:
                        res.append(x1)
            return res
        ans=[]
        S=S[1:-1]
        for x in range(1,len(S)):
            a=S[:x]
            b=S[x:]
            for x1 in foo(a):
                for x2 in foo(b):
                    ans.append("("+x1+", "+x2+")")
        return ans