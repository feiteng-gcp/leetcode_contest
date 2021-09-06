class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        string s = paragraph;
        for(int i = 0;i < s.length();i++){
            if(s[i] >= 'A' && s[i] <= 'Z') s[i] += 32;
        }
        map<string,int> mp;
        for(int i = 0;i < s.length();){
            int j = i;
            while(j + 1 < s.length() && (s[j + 1] <= 'z' && s[j + 1] >= 'a'))
                j++;
            string word = "";
            for(int k = i;k <= j;k++)
                word += s[k];
            bool flag = 1;
            for(int k = 0;k < banned.size();k++)
                if(banned[k] == word){
                    flag = 0;
                }
            if(flag) mp[word]++;
            i = j + 1;
            while(i < s.length() && (s[i] > 'z' || s[i] < 'a'))
                i++;
        }
        string ans = "";
        int ret = 0;
        for(auto x:mp){
            if(x.second > ret){
                ans = x.first;
                ret = x.second;
            }
        }
        return ans;
    }
};