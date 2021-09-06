class Solution {
public:
string mostCommonWord(string s, vector<string>& a) {
    map<string, int> ma;
    int n = s.size(), p = 0;
    while(p < n) {
        while(p < n && !isalpha(s[p])) {
            p++;
        }
        if(p >= n) break;
        int last = p;
        while(p < n && isalnum(s[p])) p++;
        string cur = s.substr(last, p - last);
        for (char & x : cur)
            x = tolower(x);
            //cout << cur << endl;
        ma[cur]++;
    }
    int r = 0;
    string res;
    set<string> se;
    for (string x : a)
        se.insert(x);
    for (auto it : ma) {
        if(!se.count(it.first)) {
            if(it.second > r) {
                r = it.second;
                res = it.first;
            }
        }
    }
    return res;
}
};