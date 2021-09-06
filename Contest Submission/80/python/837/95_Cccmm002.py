class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        bs = set()
        for b in banned:
            bs.add(b.lower())
        words = paragraph.split(' ')
        d = dict()
        for w in words:
            w = w.lower()
            nw = []
            for i in range(len(w)):
                if w[i] not in "!?',;.":
                    nw.append(w[i])
            ns = ''.join(nw)
            if ns in bs: continue
            if ns not in d:
                d[ns] = 0
            d[ns] += 1
        res = None
        r = 0
        for k in d:
            if d[k] > r:
                res = k
                r = d[k]
        return res
    