import re
import collections

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        p = paragraph.lower()
        p = re.sub("[!?',;.]", "", p)
        l = []
        for s in p.split():
            if len(s) == 0 or s in banned: continue
            l.append(s)
        r = collections.Counter(l)
        return r.most_common(1)[0][0]