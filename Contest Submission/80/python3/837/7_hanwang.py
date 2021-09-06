
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        paragraph = paragraph.lower()
        count = {}
        buf = ""
        for c in paragraph:
            if c >= 'a' and c <= 'z':
                buf += c
            else:
                if len(buf) > 0:
                    if buf not in count:
                        count[buf] = 0
                    count[buf] += 1
                buf = ""
        if len(buf) > 0:
            if buf not in count:
                count[buf] = 0
            count[buf] += 1 
        items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        dic = {}
        for b in banned:
            dic[b] = True

        for i in items:
            if i[0] not in dic:
                return i[0]

