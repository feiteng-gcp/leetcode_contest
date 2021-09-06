import re

class Solution:
    def mostCommonWord(self, paragraph, banned):
        banned = set(banned)
        count = {}
        for word in re.split("\ |\!|\?|\'|\,|\;|\.", paragraph):
            if word:
                word = word.lower()
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1
        max_count = -1
        max_word = ''
        for word, c in count.items():
            if c > max_count and word not in banned:
                max_count = c
                max_word = word
        return max_word
        
        