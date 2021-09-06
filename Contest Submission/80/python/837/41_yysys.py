import collections

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = paragraph.split(' ')
        new_words = []
        for word in words:
            new_word = ''
            for char in word:
                if char.isalpha():
                    new_word += char.lower()
            new_words.append(new_word)
        words = new_words
        c = collections.Counter()
        Max_count = 0
        ans = ''
        for word in words:
            if word not in banned:
                c[word] += 1
                if c[word] > Max_count:
                    Max_count = c[word]
                    ans = word
        return ans