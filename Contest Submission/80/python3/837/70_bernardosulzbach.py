class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        from collections import Counter
        freq = Counter()
        ban_set = set(banned)
        for word in (''.join([c.lower() for c in paragraph if c not in "!?',;."])).split(' '):
            if word and word not in ban_set:
                freq[word] += 1
        best = None
        for k in freq:
            if best is None or freq[k] > freq[best]:
                best = k
        return best