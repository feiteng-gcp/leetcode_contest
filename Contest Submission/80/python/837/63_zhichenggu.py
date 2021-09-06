class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        lst = list(paragraph.lower())
        for i in range(len(lst)):
            if ord(lst[i]) < ord('a') or ord(lst[i]) > ord('z'):
                lst[i] = ' '
        p = ''.join(lst)
        
        lst = p.split()
        
        table = {}
        b = {w:True for w in banned}
        for word in lst:
            if len(word) > 0:
                table[word] = table.get(word, 0) + 1
        
        res = ''
        v = 0
        for key, val in table.items():
            if key not in b and val > v:
                res = key
                v = val
        return res
                
            