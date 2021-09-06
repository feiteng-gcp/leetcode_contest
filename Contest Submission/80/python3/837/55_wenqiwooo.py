from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        alphabets = re.compile('[^a-zA-Z\s]')
        s = alphabets.sub('', paragraph)
        words = [x for x in s.lower().split() if x not in banned]
        counter = Counter(words)
        most_common = counter.most_common(1)
        if not most_common:
            return None
        return most_common[0][0]
    