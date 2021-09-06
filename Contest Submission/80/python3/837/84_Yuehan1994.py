class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import collections
        words = paragraph.split(" ")
        banned = set(banned)
        counts = collections.defaultdict(int)
        for word in words:
            temp = ""
            for char in word:
                if 'A' <= char <= 'Z':
                    temp += chr(ord(char) - ord('A') + ord('a'))
                elif 'a' <= char <= 'z':
                    temp += char
            if temp not in banned:
                counts[temp] += 1
        #print(counts)
        return max(counts.keys(), key=lambda x:counts[x])