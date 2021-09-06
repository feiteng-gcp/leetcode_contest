class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        words = paragraph.replace('!','').replace('?','').replace("'",'').replace(',','').replace(';','').replace('.','').split(' ')
        cnt = {}
        for w in words:
            w = w.lower()
            if not w in banned:
                if w in cnt:
                    cnt[w] += 1
                else:
                    cnt[w] = 1
        res, res_cnt = None, 0
        for w in cnt:
            if cnt[w] > res_cnt:
                res = w
                res_cnt = cnt[w]
        return res
        
        