class Solution {
 private:
  vector<string> Solve(string s) {
    vector<string> ans;
    if (to_string(stoi(s)) == s) {
      ans.push_back(s);
    }
    for (int i = 1; i < (int)s.size(); ++i) {
      string lft = s.substr(0, i), rgt = s.substr(i);
      if ((lft.size() == 1 || lft[0] != '0') && rgt.back() != '0') {
        ans.push_back(lft + '.' + rgt);
      }
    }
    return ans;
  }

 public:
  vector<string> ambiguousCoordinates(string S) {
    vector<string> ans;
    S = S.substr(1, S.size() - 2);
    for (int i = 1; i < (int)S.size(); ++i) {
      vector<string> lft = Solve(S.substr(0, i)), rgt = Solve(S.substr(i));
      for (string l : lft) {
        for (string r : rgt) {
          ans.push_back('(' + l + ", " + r + ')');
        }
      }
    }
    return ans;
  }
};