from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned=frozenset(word.lower() for word in banned)
        count=defaultdict(lambda:0)
        for word in re.split(r"[\s\!\?\'\,\;\.]+",paragraph.lower()):
            if word not in banned:
                count[word]+=1
        return sorted(list(count.items()),key=lambda p:p[1])[-1][0]