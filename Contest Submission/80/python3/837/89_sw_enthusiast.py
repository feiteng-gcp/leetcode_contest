class Solution:
    def mostCommonWord(self, paragraph, banned):
        punctuation = "!?',;."
        banned = set(banned)
        words = paragraph.lower().split()
        worddict = {}
        for word in words:
            trimmed = ''.join([c for c in word if c not in punctuation])
            if trimmed not in banned:
                worddict[trimmed] = worddict.get(trimmed, 0) + 1
        return sorted([(-v, k) for k, v in worddict.items()])[0][1]