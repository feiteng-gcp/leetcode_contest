class Solution {
public:
    bool isalpha(char c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A'  && c <= 'Z');
    }
    string mostCommonWord(string s, vector<string>& banned) {
        for (auto& it : banned) {
            for (auto& c : it) {
                if (c >= 'A' && c <= 'Z') c = c - 'A' + 'a';
            }
        }
        for (auto& it : s) {
            if (it >= 'A' && it <= 'Z') it = it - 'A' + 'a';
        }
        vector<string> words;
        for (int i = 0, j; i < s.size(); i = j) {
            for (; i < s.size() && !isalpha(s[i]); ++i);
            if (i == s.size()) break;
            for (j = i + 1; j < s.size() && isalpha(s[j]); ++j);
            words.push_back(s.substr(i, j - i));
        }
        set<string> A(banned.begin(), banned.end());
        map<string, int> cnt;
        for (auto& it : words) {
            if (A.count(it)) continue;
            cnt[it]++;
        }
        int maxv = 0;
        for (auto& it : cnt) maxv = max(maxv, it.second);
        string ret;
        for (auto& it : cnt) {
            if (it.second == maxv) ret = it.first;
        }
        return ret;
    }
};