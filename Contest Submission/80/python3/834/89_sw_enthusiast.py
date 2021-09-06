class Solution:
    def ambiguousCoordinates(self, S):
        S = S[1:-1]
        sol = []
        for i in range(1, len(S)):
            first, second = S[:i], S[i:]
            for i in range(len(first)):
                for j in range(len(second)):
                    f, s = first, second
                    if len(first) > 1:
                        f = '{0}.{1}'.format(first[:i+1], first[i+1:])
                        if f[0] == '0' and f[1] != '.':
                            f = '.'
                        if f[-1] == '0':
                            f = '.'
                    if len(second) > 1:
                        s = '{0}.{1}'.format(second[:j+1], second[j+1:])
                        if s[0] == '0' and s[1] != '.':
                            s = '.'
                        if s[-1] == '0':
                            s = '.'
                    if f == '.' or s == '.':
                        continue
                    if f[-1] == '.':
                        f = f[:-1]
                    if s[-1] == '.':
                        s = s[:-1]
                    sol.append('({0}, {1})'.format(f, s))
        return sol