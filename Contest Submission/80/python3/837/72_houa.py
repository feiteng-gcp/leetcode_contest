class Solution:
    def mostCommonWord(self, p, ban):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        t = re.split(" |\!|\?|\'|\,|\;|\.", p)
        st = set(ban)
        cnt = {}
        ans = ''
        maxc = 0
        for w in t:
            w = w.lower()
            if not w or w in st:
                continue
            if w not in cnt:
                cnt[w] = 0
            cnt[w] += 1
            if cnt[w] > maxc:
                maxc = cnt[w]
                ans = w
        return ans