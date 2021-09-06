class Solution {
private:
    vector<string> oneNum(string s) {
        int n = s.size();
        vector<string> res;
        if (stoi(s) > 0 && s[0] != '0') res.push_back(s);
        else if (stoi(s) == 0 && s.size() == 1) res.push_back(s);
        for (int i=0;i<n-1;i++) {
            string left = s.substr(0, i+1);
            string right = s.substr(i+1, n-1-i);
            if (stoi(right) <= 0) continue;
            if (right[right.size() - 1] == '0') continue;
            if (stoi(left) > 0 && left[0] == '0') continue;
            if (stoi(left) == 0 && left.size() > 1) continue;
            res.push_back(left + "." + right);
        }
        return res;
    }
    
public:
    vector<string> ambiguousCoordinates(string S) {
        vector<string> res;
        string s = S.substr(1, S.size() - 2);
        int n = s.size();
        for (int i = 0; i < n - 1; i++) {
            string left = s.substr(0, i+1);
            string right = s.substr(i+1, n-1-i);
            vector<string> lv = oneNum(left);
            if (lv.size() == 0) continue;
            vector<string> rv = oneNum(right);
            if (rv.size() == 0) continue;
            for (int l = 0;l<lv.size();l++) {
                for (int r=0;r<rv.size();r++) {
                    res.push_back("(" + lv[l] + ", " + rv[r] + ")");
                }
            }
        }
        return res;
    }
};