class Solution {
    
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        string mark = "!?',;. ";
        vector<bool>markset(300, false);
        for (char ch : mark) markset[ch] = true;
        
        unordered_set<string> bannedset(banned.begin(), banned.end());
        map<string, int> wordtable;
        
        int N = paragraph.size();
        int i = 0;
        while (i < N) {
            int j = i;
            string s = "";
            
            while (j < N && !markset[paragraph[j]]) {
                char ch = paragraph[j++];
                if (ch >= 'A' && ch <= 'Z') ch = ch - 'A' + 'a';
                s.push_back(ch);
            }
            if (!s.empty()) {
                auto it = wordtable.find(s);
                if (it == wordtable.end()) {
                    wordtable[s] = 1;
                } else ++it->second;
            }
            i = j + 1;
        }
        
        string max_wd;
        int max_cnt = -1;
        for(const auto & itr : wordtable) {
            auto it = bannedset.find(itr.first);
            if (it == bannedset.end()) {
                if (itr.second > max_cnt) {
                    max_cnt = itr.second;
                    max_wd = itr.first;
                }
            }
        }
        return max_wd;
    }
};