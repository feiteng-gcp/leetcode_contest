from collections import defaultdict
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        ban = set(banned)
        paragraph=paragraph.replace('.','')
        paragraph =paragraph.replace('?','')
        paragraph =paragraph.replace('\'', '')
        paragraph =paragraph.replace(',', '')
        paragraph =paragraph.replace(';', '')
        paragraph = paragraph.replace('!', '')
        words = paragraph.split(' ')
        count = defaultdict(int)
        for word in words:
            if word.lower() not in ban:
                count[word.lower()] += 1
        res = None
        num = 0
        for key in count:
            if count[key] > num:
                num = count[key]
                res = key
        return res
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        