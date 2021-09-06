class Solution {
public:
    int n;
    int pos;
    string str;
    char getChar(char ch) {
        if (ch >= 'A' && ch <= 'Z') return ch - 'A' + 'a';
        return ch;
    }
    
    bool isChar(char ch) {
        if (ch >= 'a' && ch <= 'z' || ch >= 'A' && ch <= 'Z') return true;
        return false;
    }
    string get() {
        string res = "";
        while (pos < n && !isChar(str[pos])) pos++;
        while (pos < n && isChar(str[pos])) {
            res += getChar(str[pos++]);
        }
        return res;
    }
    string mostCommonWord(string paragraph, vector<string>& banned) {
        map<string, int> mp;
        set<string> S(banned.begin(), banned.end());
        str = paragraph;
        n = str.size();
        pos = 0;
        while (true) {
            string tmp = get();
            if (tmp == "") break;
            if (S.find(tmp) == S.end()) {
                mp[tmp]++;
            }
            
        }
        string ans = "";
        int cnt = 0;
        for (auto p : mp) {
            if (p.second > cnt) {
                cnt = p.second;
                ans = p.first;
            }
        }
        return ans;
    }
    
};