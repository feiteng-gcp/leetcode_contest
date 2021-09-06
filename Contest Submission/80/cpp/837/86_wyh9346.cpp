class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        int first = 0;
        map<string, int> words;
        string word = "";
        for (int i = 0; i < paragraph.size(); i++) {
            if (isalpha(paragraph[i])) {
                if (!isalpha(paragraph[first])) {
                    first = i;
                }
                word += tolower(paragraph[i]);
            } else {
                if (isalpha(paragraph[first])) {
                    words[word]--;
                    first = i;
                    word = "";
                }
            }
        }
        if (word != "") {
            words[word]--;
        }
        set<string> st(banned.begin(), banned.end());
        vector<pair<int, string> > arr;
        for (auto item : words) {
            arr.push_back(make_pair(item.second, item.first));
            // cout << item.first << "\t" << item.second << endl;
        }
        sort(arr.begin(), arr.end());
        for (auto item : arr) {
            if (st.find(item.second) == st.end()) {
                return item.second;
            }
        }
        return "";
    }
};