class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        m = collections.defaultdict(int)
        paragraph = paragraph.lower()
        p = paragraph.split(' ')
        for word in p:
            start = 0 
            for i in range(len(word)):
                if word[i] in "!?',;. ":
                    if i-1 >= start and word[start:i] not in banned:
                        m[word[start:i]] += 1
                    start = i+1 
            if i-1>=start and word[start:i] not in banned:
                m[word[start:i+1]] += 1
        ans = ""
        for key in m.keys():
            if m[key] > m[ans]:
                ans = key 
        return ans 