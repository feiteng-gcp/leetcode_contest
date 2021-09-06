class Solution {
public:
    string mostCommonWord(string p, vector<string>& banned) {
        unordered_set<string> ban;
        unordered_map<string, int> table;
        for (string s : banned) ban.insert(s);
        int i = 0;
        p.push_back('!');
        for (int j = 0; j < p.size(); j++) {
            if (isalpha(p[j])) continue;
            string s = p.substr(i, j-i);
            i = j + 1;
            if (s.empty()) continue;
            for (char & c : s) {
                if ('A' <= c && c <= 'Z') c = c - 'A' + 'a';
            }
            if (ban.find(s) != ban.end()) continue;
            table[s]++;
        }
        string ret = table.begin()->first;
        for (auto it = table.begin(); it != table.end(); it++) {
            if (it->second > table[ret]) ret = it->first;
        }
        return ret;
        
        
    }
};