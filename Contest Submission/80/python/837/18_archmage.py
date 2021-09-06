from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set(ch.lower() for ch in banned)
        s = ''.join((ch.lower() if ch.isalpha() else ' ') for ch in paragraph)
        cnt = Counter(wrd for wrd in s.split(' ') if wrd and wrd not in ban)
        return list(cnt.most_common())[0][0]

