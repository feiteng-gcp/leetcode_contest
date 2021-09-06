class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        set<string> tab;
    int len = (int)banned.size();
    for(int i = 0; i < len; i++) tab.insert(banned[i]);
    
    map<string, int> cnt;
    string s;
    string& p = paragraph;
    len = (int)p.size();
    for(int i = 0; i < len; i++)
    {
        if(p[i] >= 'A' && p[i] <= 'Z') p[i] += 'a' - 'A';
        if(p[i] >= 'a' && p[i] <= 'z') s.push_back(p[i]);
        else
        {
            if(!s.empty() && !tab.count(s)) cnt[s]++;
            s.clear();
        }
    }
    if(!s.empty() && !tab.count(s)) cnt[s]++;
    int maxC = 0;
    for(auto p = cnt.begin(); p != cnt.end(); p++)
        if(p->second > maxC)
        {
            maxC = p->second;
            s = p->first;
        }
    return s;
    }
};