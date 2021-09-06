class Solution {
public:
    vector<string> ambiguousCoordinates(string S) {
        int len = S.length() - 2;
        vector<string> result;
        for (int i = 1; i < len; i++) {
            string word1 = S.substr(1, i);
            string word2 = S.substr(1+i, len - i);
            vector<string> var2;
            for (int i = 0; i < word2.length(); i++) {
                string vary = word2;
                if (i != 0) {
                    vary.insert(i, 1, '.');
                }
                if (validate(vary)) {
                    var2.push_back(vary);
                }
            }
            
            for (int i = 0; i < word1.length(); i++) {
                string vary = word1;
                if (i != 0) {
                    vary.insert(i, 1, '.');
                }
                if (validate(vary)) {
                    for (int i = 0; i < var2.size(); i++) {
                        result.push_back("(" + vary + ", " + var2[i]+")");
                    }
                }
            }
        }
        return result;
    }
private:
    bool validate(const string &str) {
        if (str[0] == '0') {
            if (str.length() != 1 && str[1] != '.') {
                return false;
            }
        }
        if (str[str.length()-1] == '0') {
            for (int i = 0; i < str.length(); i++) {
                if (str[i] == '.') {
                    return false;
                }
            }
        }
        return true;
    }
};