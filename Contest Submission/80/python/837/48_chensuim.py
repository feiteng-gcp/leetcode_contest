class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = paragraph.split(' ')
        for i in range(len(words)):
            word = words[i].lower()
            new = list()
            for char in word:
                if char.isalpha():
                    new.append(char)
            words[i] = ''.join(new)
            
        words = collections.Counter(words)
        words = words.items()
        words.sort(key=lambda x: -x[1])
        banned = set(banned)
        for word, count in words:
            if word not in banned:
                return word
        