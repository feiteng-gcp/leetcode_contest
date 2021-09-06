class Solution {
 public:
  string mostCommonWord(string paragraph, vector<string> &banned) {
    unordered_set<string> b(banned.begin(), banned.end());
    map<string, int> cnt;
    string s;
    for (char c : paragraph) {
      if (isalpha(c)) {
        s += tolower(c);
      } else {
        if (!s.empty() && b.find(s) == b.end()) {
          ++cnt[s];
        }
        s.clear();
      }
    }
    if (!s.empty() && b.find(s) == b.end()) {
      ++cnt[s];
    }
    s.clear();
    for (auto p : cnt) {
      if (s.empty() || p.second > cnt[s]) {
        s = p.first;
      }
    }
    return s;
  }
};