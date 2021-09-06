class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_set<string> bannedWords;
        for (auto& s : banned) {
            bannedWords.insert(s);
        }
        
        int n = paragraph.size();
        string p = paragraph;
        unordered_map<string,int> cnts;
        for (int i = 0; i < n; ++i) {
            if (isalpha(p[i])) {
                int j = i;
                while (i + 1 < n && isalpha(p[i + 1])) {
                    ++i;
                }
                string t;
                while (j <= i) {
                    t += tolower(p[j++]);
                }
                ++cnts[t];
            }
        }
        
        string res;
        int cnt = 0;
        
        for (auto& p : cnts) {
            if (bannedWords.count(p.first) == 0 && p.second > cnt) {
                res = p.first;
                cnt = p.second;
            }
        }
        
        return res;
    }
};