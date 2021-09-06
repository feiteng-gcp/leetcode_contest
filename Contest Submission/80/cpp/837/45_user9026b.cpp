class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        
        unordered_set<string> setBanned;
        for (int i = 0; i < banned.size(); ++i)
            setBanned.insert( banned[i] );
        
        int maxVal = 0;
        string result = "";
        unordered_map<string, int> hash;
        for (int i = 0; i < paragraph.size(); ++i)
        {
            if ( isalpha(paragraph[i]) != 0 )
            {
                string word = "";
                i = GetStr(paragraph, i, word);
                if (setBanned.find(word) == setBanned.end()) 
                {
                    hash[word]++;
                    if (hash[word] > maxVal)
                    {
                        maxVal = hash[word];
                        result = word;
                    }
                }
            }
        }
        
        return result;
    }
    
    int GetStr(string& s ,int i, string& word)
    {
        word = "";
        for (; i < s.size() && isalpha(s[i]) != 0; ++i)
        {
            if (s[i] >= 'A' && s[i] <= 'Z') word += char(s[i] + 32);
                                       else word += s[i];
        }
        return i - 1;
    }
};