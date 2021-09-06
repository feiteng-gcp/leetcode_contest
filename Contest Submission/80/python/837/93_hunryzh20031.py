class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = paragraph.split()
        stat = collections.defaultdict(int)
        banned_set = set(banned)
        punc = "!?',;."
        for word in words:
            w = word
            if word[-1] in punc:
                w = word[:-1]
            w = w.lower()
            if w not in banned_set:
                stat[w] += 1
        most_freq = 0
        most_freq_w = None
        for k in stat:
            if stat[k] > most_freq:
                most_freq = stat[k]
                most_freq_w = k
        return most_freq_w
        