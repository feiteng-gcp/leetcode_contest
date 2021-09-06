class Solution {
public:
    string mostCommonWord(string s, vector<string>& banned) {
        for(int i=0;i<s.size();i++){
            s[i]=tolower(s[i]);
            if( !(s[i]>='a' && s[i]<='z') ){
                s[i]=' ';
            }    
        }
        
        map<string,int>m;
        istringstream is(s);
        string aux;
        while(is>>aux){
            m[aux]++;
        }
        
        vector<pair<string,int> >v(m.begin(),m.end());
        int maxi=-1;
        set<string>S;
        
        for(int i=0;i<banned.size();i++){
            for(int j=0;j<banned[i].size();j++)
                banned[i][j]=tolower(banned[i][j]);
            S.insert(banned[i]);
        }
        
        string ans="";
        for(int i=0;i<v.size();i++){
            if(S.find(v[i].first)==S.end() ){
                if(v[i].second>maxi){
                    maxi=v[i].second;
                    ans=v[i].first;
                }
            }
        }
        
        return ans;
    }
};