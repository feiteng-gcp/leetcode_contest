class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        paragraph = paragraph.lower().strip()
        paragraph = paragraph.replace('!', '')
        paragraph = paragraph.replace('?', '')
        paragraph = paragraph.replace('\'', '')
        paragraph = paragraph.replace(',', '')
        paragraph = paragraph.replace(';', '')
        paragraph = paragraph.replace('.', '')

        data = paragraph.split(' ')

        banList = {}
        for c in banned:
            banList[c] = True

        hashMap = {}
        for word in data:
            if word in banList:
                continue
            if word in hashMap:
                hashMap[word] += 1
            else:
                hashMap[word] = 1

        ans = ''
        time = -1

        for key in hashMap:
            if hashMap[key] > time:
                time = hashMap[key]
                ans = key
        return ans