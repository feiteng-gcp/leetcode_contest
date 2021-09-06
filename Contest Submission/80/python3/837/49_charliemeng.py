from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        paragraph = re.sub(r"!|\?|\'|,|;|\.", '', paragraph)
        count = Counter(paragraph.lower().split(' '))
        bs = set(banned)
        for s in count.most_common(len(count)):
            if s[0] not in bs: return s[0]