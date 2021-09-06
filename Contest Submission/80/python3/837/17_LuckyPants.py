class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        banned = set(banned)
        xx = ''.join([_ if 'a'<=_<='z' or _==' ' else '' for _ in paragraph.lower()])
        xx = xx.split()
        dic = collections.Counter(xx)
        
        x, ret = 0, None
        for k in dic:
            if k not in banned:
                if dic[k]>x:
                    x = dic[k]
                    ret = k
        return ret