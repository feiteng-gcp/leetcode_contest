class Solution {
public:
    string get_str(string &str, int &cur, int n) {
        string result;
        while (cur < n && isalpha(str[cur])) {
            result.push_back(tolower(str[cur++]));
        }
        return result;
    }
    string mostCommonWord(string str, vector<string>& banned) {
        unordered_map<string, int> count;
        unordered_set<string> blacklist;
        for (auto cur : banned) {
            blacklist.insert(cur);
        }
        int n = str.length(), cur = 0;
        while (cur < n) {
            while (cur < n && !isalpha(str[cur])) cur++;
            if (cur < n) {
                string cur_str = get_str(str, cur, n);
                if (blacklist.count(cur_str) == 0) count[cur_str]++;
            }
        }
        int max_count = 0;
        string result = "";
        for (auto cur : count) {
            if (cur.second > max_count) {
                max_count = cur.second;
                result = cur.first;
            }
        }
        return result;
    }
};