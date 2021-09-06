class Solution {
public:
    char lower(char c) {
        return c >= 'A' && c <= 'Z' ? c - 'A' + 'a' : c;
    }
    bool alpha(char c) {
        return lower(c) >= 'a' && lower(c) <= 'z';
    }
    string mostCommonWord(string paragraph, vector<string>& banned) {
        map<string, int> cnt;
        int n = paragraph.size();
        int i = 0;
        while (i < n) {
            int j = i;
            if (alpha(paragraph[i])) {
                while (i < n && alpha(paragraph[i])) i++;
                string s = paragraph.substr(j, i - j);
                for (char& c: s) c = lower(c);
                cnt[s]++;
            } else {
                i++;
            }
        }
        for (string s: banned) {
            cnt[s] = 0;
        }
        cnt[""] = 0;
        string ret = "";
        for (auto pr: cnt) {
            if (pr.second > cnt[ret])
                ret = pr.first;
        }
        return ret;
    }
};