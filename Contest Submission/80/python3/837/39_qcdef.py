import re

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set()
        for word in banned:
            ban.add(word.lower())
        counts = {}
        maxcount = 0
        maxword = ''
        for word in paragraph.split():
            r = re.compile(r'[^-A-Za-z0-9]')
            w = r.sub('', word.lower())
            if w not in ban:
                if w not in counts:
                    counts[w] = 0
                counts[w] += 1
                if counts[w] > maxcount:
                    maxcount = counts[w]
                    maxword = w
        return maxword