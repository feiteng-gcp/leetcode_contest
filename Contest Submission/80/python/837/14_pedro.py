from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        punc = set("\"!?',;.")
        banned = set(banned)
        ct = Counter()
        for word in paragraph.split():
            word = ''.join([c for c in word if c not in punc]).lower()
            if word not in banned:
                ct[word] += 1
        return ct.most_common(1)[0][0]
        