class Solution {
	public:
		bool is_punctuation(const char ch) {
			return ch == '!' || ch == '?' || ch == ',' || ch == ';' || ch == '.' || ch == '\'';
		}
		string mostCommonWord(string paragraph, vector<string>& banned) {
            map<string, int> cnt;
			string word;
			for (const char &ch: paragraph) {
				if (is_punctuation(ch)) {
                    continue;
                } else if (ch == ' ') {
                    cnt[word] ++;
                    word = "";
                } else {
                    if (ch >= 'A' && ch <= 'Z') {
                        word += ch + 32;
                    } else {
                        word += ch;
                    }
                }
			}
            if (word != "") {
                cnt[word] ++;
            }
            int freq = 0;
            string answer;
            for (const auto &t: cnt) {
                bool ok = true;
                for (const string &s: banned) {
                    if (s == t.first) {
                        ok = false;
                    }
                }
                if (ok) {
                    if (t.second > freq) {
                        freq = t.second;
                        answer = t.first;
                    }
                }
            }

            return answer;
		}
};
