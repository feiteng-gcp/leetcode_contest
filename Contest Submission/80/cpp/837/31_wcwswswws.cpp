class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_set<string> banned_set;
        for (const auto& iter : banned) {
            banned_set.insert(iter);
        }
        string ans, temp;
        int ans_cnt = 0;
        unordered_map<string, int> dict;
        for (int i = 0; i < paragraph.length(); i++) {
            char ch = paragraph[i];
            if (ch >= 'A' && ch <= 'Z') {
                ch = ch - 'A' + 'a';
            }
            if (ch < 'a' || ch > 'z') {
                if (temp.empty()) { continue; }
                if (banned_set.find(temp) == banned_set.end()) {
                    dict[temp]++;
                    if (dict[temp] > ans_cnt) {
                        ans_cnt = dict[temp];
                        ans = temp;
                    }
                }
                temp = "";
            } else {
                temp += ch;
            }
        }
        dict[temp]++;
        if (dict[temp] > ans_cnt) {
            ans = temp;
        }
        return ans;
    }
};