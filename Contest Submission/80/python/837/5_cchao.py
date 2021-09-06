from collections import Counter

class Solution(object):
    def mostCommonWord(self, s, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        s = map(lambda x : x.lower(), s)
        s = map(lambda x : x if x.islower() else ' ', s)
        s = ''.join(s)
        s = s.split()
        s = filter(lambda x : x not in banned, s)
        cnt = Counter(s)
        return cnt.most_common(1)[0][0]
