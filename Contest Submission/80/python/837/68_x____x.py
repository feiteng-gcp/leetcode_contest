class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set((w.lower() for w in banned))
        c = {}
        for x in '!?\',;.':
            paragraph = paragraph.replace(x, ' ')
        for w in filter(None, paragraph.split()):
            w1 = w.lower()
            if w1 not in banned:
                c[w1] = c.get(w1, 0) + 1
        x = max(c.values())
        for w in c:
            if c[w] == x:
                return w
        return ''
        