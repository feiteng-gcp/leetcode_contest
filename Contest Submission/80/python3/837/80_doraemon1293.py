class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        from collections import Counter
        import re
        banned=set(banned)
        paragraph=Counter(re.split(r"[\W]+",paragraph.lower()))
        print(paragraph)
        for word,v in paragraph.most_common():
            if word and word not in banned:
                return word