class Solution:
    def mostCommonWord(self, par, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for s in "!?',;.":
          par = par.replace(s, "")
        par = par.lower()
        from collections import Counter
        banned = set(banned)
        par = [p for p in par.strip().split() if not p in banned]
        return Counter(par).most_common(1)[0][0]
      
        
        