class Solution {
public:
    bool valid(const string &s, bool flag) {
        if (s.length() >= 2 && s[0] == '0' && s[1] != '.') {
            return false;
        }
        if (s.back() == '.') {
            return false;
        }
        if (flag && s.back() == '0') {
            return false;
        }
        return true;
    }
    vector<string> getValid(const string &s) {
        // cout << "s = " << s << endl;
        vector<string> res;
        if (valid(s, false)) {
            res.push_back(s);
        }
        for (int i = 0; i < s.length() - 1; i++) {
            if (valid(s.substr(0, i + 1) + "." + s.substr(i + 1), true)) {
                res.push_back(s.substr(0, i + 1) + "." + s.substr(i + 1));
            }
        }
        return res;
    }
    vector<string> ambiguousCoordinates(string S) {
        S = S.substr(1, S.length() - 2);
        vector<string> res;
        for (int i = 0; i < S.length() - 1; i++) {
            vector<string> lvalid = getValid(S.substr(0, i + 1));
            vector<string> rvalid = getValid(S.substr(i + 1));
            for (string l : lvalid) {
                for (string r : rvalid) {
                    res.push_back("(" + l + ", " + r + ")");
                }
            }
        }
        return res;
    }
};