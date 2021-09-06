class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        for (auto& c : paragraph) {
            if (c >= 'A' && c <= 'Z') c = c - 'A' + 'a';
        }
        paragraph += " ";
        vector<string> words;
        string current;
        for (auto& c : paragraph) {
            if (c >= 'a' && c <= 'z') {
                current += c;
            } else {
                if (!current.empty()) words.push_back(current);
                current.clear();
            }
        }
        map<string, int> m;
        for (auto& w : words) {
            m[w]++;
        }
        for (auto& b : banned) {
            m[b] = 0;
        }
        int maxi = 0;
        string maxt = "";
        for (auto& w : m) {
            if (maxi < w.second) {
                maxi = w.second;
                maxt = w.first;
            }
        }
        return maxt;
    }
};