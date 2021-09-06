class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        set<string> bs;
        
        for(string b : banned){
            bs.insert(b);
        }
        
        unordered_map<string, int> freq;
        
        string disallowed = "!?',;.";
        
        
        string best = "";
        
        
        
        stringstream ss(paragraph);
        
        string tok;
        
        while(ss >> tok){
            string build;
            for(int i=0; i<tok.size(); i++){
                if(disallowed.find(tok[i]) == -1){
                    build.append(1, tolower(tok[i]));
                }
            }
            
            if(bs.count(build)) continue;
            
            freq[build]++;
            if(freq[build] >= freq[best]) best = build;
        }
        
        
        return best;
        
        
        
    }
};