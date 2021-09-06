class Solution {
    vector<string> make_word(string & s, int i, int j) {
        vector<string> ret;
        if (i+1 == j) {
            ret.push_back(string(1, s[i]));
            return ret;
        }
        if (s[i] == '0') {
            if (s[j-1] != '0') ret.push_back("0."+s.substr(i+1, j-i-1));
            return ret;
        }
        ret.push_back(s.substr(i, j-i));
        for (int k = i+1; k < j && s[j-1] != '0'; k++) {
            ret.push_back(s.substr(i, k-i) + "." + s.substr(k, j-k));
        }
        return ret;
    }
public:
    vector<string> ambiguousCoordinates(string S) {
        int n = S.size();
        vector<string> ret;
        for (int i = 2; i < n-1; i++) {
            vector<string> tmp1 = make_word(S, 1, i);
            vector<string> tmp2 = make_word(S, i, n-1);
            for (string & s1 : tmp1) {
                for (string & s2 : tmp2) {
                    ret.push_back("(" + s1 + ", " + s2 + ")");
                }
            } 
        }
        return ret;
        
    }
};