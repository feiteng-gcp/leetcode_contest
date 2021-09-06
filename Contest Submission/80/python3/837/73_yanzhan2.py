class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = paragraph.split()
        banned = set(banned)
        counter = collections.Counter()
        symbols = "!?',;."
        for word in words:
            word = word.lstrip(symbols).rstrip(symbols).lower()
            if word not in banned:
                counter[word] += 1
        return counter.most_common(1)[0][0]