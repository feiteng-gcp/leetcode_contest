class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_set<string> ban{banned.begin(),banned.end()};
        unordered_map<string,int> m;
        string str;
        for(auto i:paragraph) {
            if(isalpha(i)) {
                str.push_back(tolower(i));
            } else {
                if(!str.empty() && ban.count(str)==0) {
                    m[str]+=1;
                }
                str.clear();
            }
        }
        if(!str.empty() && ban.count(str)==0) {
                    m[str]+=1;
        }
        pair<string,int> res("",0);
        for(auto &i:m) {
            if(i.second>res.second) {
                res = i;
            }
        }
        return res.first;
    }
};