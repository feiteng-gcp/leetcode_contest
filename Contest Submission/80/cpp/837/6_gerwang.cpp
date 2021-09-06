class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        int idx=0,n=paragraph.length();
        map<string,int> ms;
        for(auto& ban:banned) {
            ms[ban]=-1;
        }
        int best=0;
        string ans="";
        while(idx<n) {
            while(idx<n&&!isalpha(paragraph[idx])) {
                idx++;
            }
            if(idx<n) {
                int end_idx=idx;
                string tmp="";
                while(end_idx<n&&isalpha(paragraph[end_idx])) {
                    tmp+=tolower(paragraph[end_idx]);
                    end_idx++;
                }
                int& t=ms[tmp];
                if(t!=-1) {
                    t++;
                    if(best<t) {
                        best=t;
                        ans=tmp;
                    }
                }
                idx=end_idx;
            }
        }
        return ans;
    }
};