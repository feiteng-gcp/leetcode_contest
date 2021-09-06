class Solution {
public:
    vector<string> g(string s) {
        vector<string> candidates{s};
        for (size_t i = 1; i < s.size(); i++) {
            auto copy = s;
            copy.insert(begin(copy) + i, '.');
            candidates.push_back(copy);
        }
        vector<string> good;
        for (auto candidate : candidates) {
            // Cannot start with a 0 if not "0.".
            if (candidate[0] == '0') {
                if (candidate.size() > 1 && candidate[1] != '.') {
                    continue;
                }
            }
            // Cannot end with "0" if there is a period.
            if (candidate.back() == '0' && count(begin(candidate), end(candidate), '.') == 1) {
                continue;
            }
            good.push_back(candidate);
        }
        return good;
    }
    vector<string> ambiguousCoordinates(string s) {
        vector<string> answers;
        s.erase(s.begin());
        s.pop_back();
        for (size_t i = 1; i < s.size(); i++) {
            const auto va = g(s.substr(0, i));
            const auto vb = g(s.substr(i));
            for (auto a : va) {
                for (auto b : vb) {
                    answers.push_back("(" + a + ", " + b + ")");
                }
            }
        }
        return answers;
    }
};