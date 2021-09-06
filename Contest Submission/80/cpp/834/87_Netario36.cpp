class Solution {
private:
    void work(string s, vector<string>& ans){
        for (int i = 1; i < s.size(); ++ i){
            string p = s.substr(0, i), q = s.substr(i, s.size() - i);
            long long vp = stol(p), vq = stol(q);
            if (to_string(vp) + q != s) continue;
            if (vq % 10 == 0) continue;
            ans.push_back(p + "." + q);
        }
    }
    
public:
    vector<string> ambiguousCoordinates(string S) {
        vector<string> ans;
        S = S.substr(1, S.size() - 2);
        for (int i = 1; i < S.size(); ++ i){
            vector<string> l, r;
            string a = S.substr(0, i), b = S.substr(i, S.size() - i);
            long long va = stol(a), vb = stol(b);
            if (to_string(va) + b == S){
                l.push_back(to_string(va));
            }
            if (a + to_string(vb) == S){
                r.push_back(to_string(vb));
            }
            work(a, l);
            work(b, r);
            for (auto& lx : l)
                for (auto& rx : r)
                    ans.push_back("(" + lx + ", " + rx + ")");
        }
        return ans;
    }
};