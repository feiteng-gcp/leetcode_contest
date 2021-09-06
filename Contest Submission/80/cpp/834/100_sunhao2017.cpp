class Solution {
public:
    vector<string> ambiguousCoordinates(string s) {
        int n = s.length() - 1;
        vector<string> result;
        for (int comma = 1; comma < n - 1; comma++) {
            string left_str = s.substr(1, comma);
            string right_str = s.substr(comma + 1, n - comma - 1);
            vector<string> left = get_result(left_str), right = get_result(right_str);
            for (auto cur_left : left) {
                for (auto cur_right : right) {
                    result.push_back("(" + cur_left + ", " + cur_right + ")");
                }
            }
        }
        return result;
    }
    
    vector<string> get_result(string &s) {
        int n = s.length();
        vector<string> result;
        if (n == 1) {
            result.push_back(s);
        } else {
            if (s[0] != '0') result.push_back(s);
        }
        for (int dot = 0; dot < n - 1; dot++) {
            string left = s.substr(0, dot + 1), right = s.substr(dot + 1);
            //cout << left << " " << right << endl;
            string check_left = to_string(stoll(left)), check_right = to_string(stoll(right));
            if (left == check_left && check_right != "0") {
                string cur_result = left + "." + right;
                if (cur_result.back() != '0') {
                    result.push_back(cur_result);
                }
            }
        }
        return result;
    }
};