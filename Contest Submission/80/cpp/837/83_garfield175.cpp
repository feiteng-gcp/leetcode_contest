class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_set<string> bannedSet;
        for(auto ban : banned) {
            bannedSet.insert(ban);
        }
        for(int i = 0; i < paragraph.length(); i++) {
            if (paragraph[i] >= 'A' && paragraph[i] <= 'Z') {
                paragraph[i] = paragraph[i] - 'A' + 'a';
            }
        }
        unordered_map<string, int> counts;
        int start = 0;
        for(int i = 0; i <= paragraph.length(); i++) {
            if (i == paragraph.length() ||
                !(paragraph[i] >= 'a' && paragraph[i] <= 'z' || paragraph[i] >= 'A' && paragraph[i] <= 'Z')) {
                if (start < i) {
                    string word = paragraph.substr(start, i - start);
                    if (! bannedSet.count(word)) {
                        counts[word]++;
                    }
                    // cout << word << endl;
                }
                start = i + 1;
            }
        }
        int maxCount = 0;
        string maxString = "";
        for(auto count : counts) {
            if (maxCount < count.second) {
                maxString = count.first;
                maxCount = count.second;
            }
            // cout << count.first << ", " << count.second << endl;
        }
        return maxString;
    }
};