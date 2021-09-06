class Solution {
public:
    string mostCommonWord(string s, vector<string>& ban) {
        int l = 0; 
        string best = "";
        map<string, int> M;
        for (int i = 0; i < s.size(); ++i) if (!isalpha(s[i])) s[i]=' '; else s[i]=tolower(s[i]); 
        istringstream iss(s);
        
        set<string> B; for (string x : ban) B.insert(x);
        string x;
        while(iss >> x) {
            if (!B.count(x)) {
                M[x]++;
                if (M[x]>l) {l = M[x]; best=x;}
            }
        }
        return best;
    }
};