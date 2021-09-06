class Solution {
public:
pair<bool, vector<string>> work(string & s) {
    if(s.size() == 1) {
        return {1, {s} };
    }
    int n = s.size();
    if(s[0] == '0') {
        if(s[n - 1] == '0') {
            return {0, {} };
        }
        return {1, {"0." + s.substr(1)  } };
    }
    if(s[n - 1] == '0') {
        return {1, {s} };
    }
    vector<string> res;
    res.push_back(s);
    for (int i = 1; i < n; i++) {
        string cur = s.substr(0, i) + "." + s.substr(i);
        res.push_back(cur);
    }
    return {1, res};
}
vector<string> ambiguousCoordinates(string s) {
    int n = s.size();
    vector<string> res;
    for (int i = 2; i < n - 1; i++) {
        string x = s.substr(1, i - 1), y = s.substr(i, n - 1 - i);
        pair<bool, vector<string>> a = work(x), b = work(y);
        if(a.first && b.first) {
            for (string x1 : a.second) {
                for (string x2 : b.second) {
                    stringstream ss;
                    ss << "(" << x1 << ", " << x2 << ")";
                    res.push_back(ss.str());
                }
            }
        }
    }
    return res;
}
};