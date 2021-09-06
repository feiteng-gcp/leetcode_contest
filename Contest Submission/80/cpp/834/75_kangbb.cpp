class Solution {
public:
    vector<string> posa;
    vector<string> posb;
    
    bool check(string d, string f) {
        int nd = d.length();
        int nf = f.length();
        if (nd == 0) return false;

        double dp = atof(d.c_str());
        double fp = atof(f.c_str());

        // digital part has ending 0
        if (f.back() == '0') return false;

        if (dp > 0 && d[0] == '0') return false;

        // decimal part has leading zeros 00 or 000, etc
        if (nd > 1 && d[0] == '0' && d[1] == '0') return false;
        return true;
    }

    void search(string a, vector<string>& pos) {
        int n = a.length();
        if (check(a, string(""))) pos.push_back(a);

        string d;
        string f;
        for (int i = 1; i < n; ++i) {
            d = a.substr(0, i);
            f = a.substr(i);
            // cout << d << " " << f << endl;
            if (check(d, f)) {
                string newa = d + '.' + f;
                pos.push_back(newa);
                //    cout << newa << endl;
            }

        }
    }
    vector<string> ambiguousCoordinates(string S) {
        // commas, decimal points, and spaces
        vector<string> sol;
        int n = S.length();
        string a;
        string b;
        for (int i = 1; i < n - 2; ++i) {
            a = S.substr(1, i);
            b = S.substr(1 + i, n - i - 2);
            cout << "[" << a << "] [" << b << "]" << endl;
            search(a, posa);
            search(b, posb);

            if (posa.size() && posb.size()) {
                for (auto sa: posa) {
                    for (auto sb: posb) {
                        string tmp;
                        tmp += "(";
                        tmp += sa;
                        tmp += ", ";
                        tmp += sb;
                        tmp += ")";
                        sol.push_back(tmp);
                    }
                }

            }
            posa.clear();
            posb.clear();
        }
        return sol;
    }
};