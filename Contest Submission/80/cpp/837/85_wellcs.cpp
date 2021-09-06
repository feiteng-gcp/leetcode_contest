class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        string ret;
        int maxNum = 0;
        set<string> bannedSet(banned.begin(), banned.end());
        string cur;
        set<char> punc = {'!', '?', '\'', ',', ';', '.'};
        vector<string> words;
        for(auto c : paragraph)
        {
            c = (char)tolower(c);
            if(punc.count(c) != 0)
            {
                continue;
            }
            
            if(c == ' ')
            {
                if(cur.length() > 0)
                {
                    words.push_back(cur);
                    cur = "";
                    continue;
                }
            }
            else
            {
                cur += c;
            }
        }
        
        if(cur.length() > 0)
        {
            words.push_back(cur);
        }
        
        map<string, int> m;
        for(auto& w : words)
        {
            if(bannedSet.count(w) != 0)
            {
                continue;
            }
            m[w]++;
            if(m[w] > maxNum)
            {
                maxNum = m[w];
                ret = w;
            }
        }
        
        return ret;
    }
};