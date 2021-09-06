class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
       
        for(int i = 0; i < paragraph.size(); ++i){
            if(isalpha(paragraph[i])){
                paragraph[i] = tolower(paragraph[i]);
            }
        }
       // cout << paragraph << endl;
        
        set<string> bans(banned.begin() , banned.end());
        
        map<string,int> mp;
        int n = paragraph.size();
        int last = -1;
        for(int i = 0; i <= n; ++i){
            if(i == n || !islower(paragraph[i]) ){
                if(last != -1){
                    string word = paragraph.substr(last , i - last);
                  //  cout << word<< endl;
                    if(bans.find(word) == bans.end()){
                        mp[word]++;
                    }     
                }
                last = -1;
            }else{
                if(last == -1){
                    last = i;
                }
            }
        }
        string ret;
        int ans = -1;
        for(auto it : mp){
            if(it.second > ans){
                ans = it.second;
                ret = it.first;
            }
        }
        return ret;
    }
};