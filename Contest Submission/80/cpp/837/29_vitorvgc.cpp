class Solution {
public:
    
    string lower(string s) {
        string ans;
        for(char c : s)
            ans += tolower(c);
        return ans;
    }
    
    string mostCommonWord(string paragraph, vector<string>& banned) {
        
        string ans;
        int mx = 0;
        map<string ,int> mp;
        unordered_set<string> st;
        for(auto s : banned)
            st.insert(s);
        
        string text = lower(paragraph);

        for(stringstream ss(text); ss.good(); ) {
            string s;
            ss >> s;
            
            while(!s.empty() && !isalpha(s.back()))
                s.pop_back();
            
            if(st.find(s) != st.end()) continue;
            
            int q = ++mp[s];
            if(q > mx)
                mx = q, ans = s;            
        }
        
        return ans;
    }
};