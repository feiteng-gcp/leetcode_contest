class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_map<string,int> nmap;
        string res = "";
        int num = 0;
        unordered_set<string> ban(banned.begin(),banned.end());
        
        for(int i = 0;i<paragraph.length();i++)
        {
            if(paragraph[i]<='z'&&paragraph[i]>='a')
            {
                res = res+paragraph[i];
            }
            else if(paragraph[i]<='Z'&&paragraph[i]>='A')
            {
                res = res+char(tolower(paragraph[i]));
            }
            else
            {
                if(ban.count(res)==0&&res!="")
                {
                    nmap[res]++;
                }
                res = "";
            }
        }
        
        if(res!=""&&ban.count(res)==0)
        {
            nmap[res]++;
        }
        
        for(auto i = nmap.begin();i!=nmap.end();i++)
        {
            if(i->second>num)
            {
                num = i->second;
                res = i->first;
            }
        }
        
        return res;
    }
};