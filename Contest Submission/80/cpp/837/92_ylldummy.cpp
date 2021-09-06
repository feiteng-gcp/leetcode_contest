class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        set<string> banSet;
        map<string, int> countMap;
        const string separators = "!?',;. ";
        int start = 0, end = 0;
        int maxCount = 0;
        string result;
        
        paragraph += "."; // ensure end
        
        for (int i = 0; i < banned.size(); i++) {
            banSet.insert(banned[i]);
        }
        
        while (end < paragraph.length()) {
            bool isEnd = false;
            for (int i = 0; i < separators.length(); i++) {
                if (paragraph[end] == separators[i]) {
                    isEnd = true;
                    break;
                }
            }
            if (isEnd) {
                if (start != end) {
                    string word = paragraph.substr(start, end-start);
                    transform(word.begin(), word.end(), word.begin(), ::tolower);
                    auto it = countMap.find(word);
                    if (banSet.find(word) == banSet.end()) {
                        if (it == countMap.end()) {
                            countMap[word] = 1;
                        } else {
                            it->second++;
                        }
                    }
                }
                end++;
                start = end;
            } else {
                end++;
            }
        }
        
        for (auto it : countMap) {
            if (it.second > maxCount) {
                maxCount = it.second;
                result = it.first;
            }
        }
        return result;
    }
};