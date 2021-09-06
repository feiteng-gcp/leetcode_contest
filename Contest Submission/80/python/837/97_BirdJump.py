class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        from collections import Counter
        
        C=Counter()
        paragraph="".join([x for x in paragraph if x not in "!?',;."]).lower()
        C=Counter(paragraph.split())
        
        for word,num in C.most_common():
            if word not in banned:
                return word