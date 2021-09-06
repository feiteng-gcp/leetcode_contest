from collections import defaultdict

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        paragraph = paragraph.lower()
        
        paragraph = ''.join(c for c in paragraph if c in 'abcdefghijklmnopqrstuvwxyz ')
        
        words = paragraph.split()
        words = [word.strip() for word in words]
        
        counts = defaultdict(int)
        best = ""
        for word in words:
            if word in banned:
                continue
            counts[word] += 1
            if counts[word] > counts[best]:
                best = word
        return best
        