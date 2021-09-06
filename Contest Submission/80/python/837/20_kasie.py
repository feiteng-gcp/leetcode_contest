import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        a = re.split("[ !?',;.]", paragraph)
        for i in range(len(a)):
            a[i] = a[i].lower()
        for i in range(len(banned)):
            banned[i] = banned[i].lower()
        cnt = {}
        for word in a:
            if word not in cnt: cnt[word] = 0
            cnt[word] += 1
        ans = 0
        ans_word = None
        for word, c in cnt.items():
            if word in banned: continue
            if word == '': continue
            if ans < c:
                ans = c
                ans_word = word
        return ans_word