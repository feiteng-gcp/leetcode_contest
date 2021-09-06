class Solution {
public:
    #define mp make_pair
    #define pii pair<int, string>
    string mostCommonWord(string paragraph, vector<string>& banned) {
        int n = banned.size();
        string s = "!?',;.";
        for( int i = 0 ; i < paragraph.size();  ++i ){
            for( int j = 0 ; j < s.size(); ++j ){
                if( paragraph[i] == s[j] ){
                    paragraph[i] = ' ';
                    break;
                }
            }
        }
        
        stringstream ss(paragraph);
        
        unordered_map<string,int> m;
        while( ss>>s ){
            for( int i = 0 ; i < s.size() ; ++i ) s[i] = tolower(s[i]);
            m[ s ]++;
        }
        vector< pii > v;
        for( auto it:m ){
            v.push_back( mp(it.second, it.first));
        }
        sort( v.rbegin(), v.rend() );
        
        for( int i = 0 ; i < v.size() ; ++i ){
            bool b = true;
            for( int j = 0 ; j < n ; ++j ){
                if( v[i].second == banned[j] ){
                    b= false;
                    break;
                }
            }
            if( b ) return v[i].second;
        }
        return "";
    }
};