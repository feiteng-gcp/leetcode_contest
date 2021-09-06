class Solution {
    bool is_valid(const string &s){
        if(s.empty()) return false;
        if(s.size() == 1) return true;
        int n = s.size();
        int dotcnt = 0;
        if(s[0] == '0'){
            if(s[1] != '.') return false;
        }
        for(int i=0;i<n;i++){
            if(s[i] == '.'){
                if(++dotcnt > 1) return false;
            }
        }
        
        if(dotcnt > 0 && s[n-1] == '0') return false;
        
        return true;
    }
public:
    vector<string> ambiguousCoordinates(string S) {
        int n = S.size()-2;
        S = S.substr(1, n);
        vector<vector<set<string>>> dp(n, vector<set<string>>(n));
        for(int i=0;i<n;i++) dp[i][i].insert(string(1,S[i]));
        for(int len=2;len<=n;len++){
            for(int i=0;i<=n-len;i++){
                int j = i + len - 1;
                for(const string &t : dp[i][j-1]){
                    string t2 = t;
                    t2.push_back(S[j]);
                    dp[i][j].insert(t2);
                    t2.pop_back();
                    t2.push_back('.');
                    t2.push_back(S[j]);
                    dp[i][j].insert(t2);
                }
            }
        }
        
        set<string> ans;
        for(int i=1;i<n;i++){
            for(const string &left : dp[0][i-1]){
                if(!is_valid(left)) continue;
                for(const string &right : dp[i][n-1]){
                    if(!is_valid(right)) continue;
                    ans.insert("(" + left + ", " + right + ")");
                }
            }
        }
        
        // cout << is_valid("10") << ' ' << is_valid("0") << endl;
        
        return vector<string>(ans.begin(), ans.end());
    }
};