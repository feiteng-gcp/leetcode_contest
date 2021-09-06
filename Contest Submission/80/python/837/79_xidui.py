from collections import defaultdict

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        paragraph = paragraph.replace(';', ' ')
        paragraph = paragraph.replace(',', ' ')
        paragraph = paragraph.replace('.', ' ')
        paragraph = paragraph.replace('!', ' ')
        paragraph = paragraph.replace('?', ' ')
        paragraph = paragraph.replace("'", ' ')
        words = paragraph.split()
        dic = defaultdict(int)
        for word in words:
            if word and word not in banned:
                dic[word] += 1
        
        most = 0
        ans = ""
        for k, v in dic.items():
            if v > most:
                most = v
                ans = k
        return ans
        