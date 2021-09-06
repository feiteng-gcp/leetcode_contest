class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        newparagraph = ''
        for c in paragraph.lower():
            if c in '!?\',;.': continue
            newparagraph += c
        words = newparagraph.split()
        banned = set(banned)
        cnt = {}
        for w in words:
            if w not in banned:
                if w not in cnt:
                    cnt[w] = 0
                cnt[w] += 1
        
        max_cnt, max_word = 0, None
        for w in cnt:
            if cnt[w] > max_cnt:
                max_cnt, max_word = cnt[w], w
        return max_word
