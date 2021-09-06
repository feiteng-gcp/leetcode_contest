from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        l=paragraph.lower().split(' ')
        d=defaultdict(int)
        b=set(banned)
        for w in l:
            if len(w)==0:
                continue
            if not w[-1].isalpha():
                w=w[:-1]
            if len(w)>0:
                d[w]+=1
        ans=0
        ret=''
        for w in d:
            if w not in b and d[w]>ans:
                ans=d[w]
                ret=w
        return ret
                
            
        