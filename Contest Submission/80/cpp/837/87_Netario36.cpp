class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_set<string> hash;
        unordered_map<string, int> cnt;
        for (auto& x: banned)
            hash.insert(x);
        string tmp = "";
        for (auto c : paragraph){
            c = tolower(c);
            if (islower(c)){
                tmp += string(1, c);
            }
            if (c == ' '){
                if (hash.count(tmp) == 0){
                    cnt[tmp] ++; 
                }
                tmp = "";
            }
        }
        if (tmp != "" && hash.count(tmp) == 0) cnt[tmp] ++;
        vector<pair<string, int>> arr;
        for (auto& p : cnt){
            //cout << p.first << ' ' << p.second << endl;
            arr.push_back(p);
        }
        auto cmp = [](pair<string, int>& a, pair<string, int>& b){ return a.second > b.second; };
        sort(arr.begin(), arr.end(), cmp);
        return arr.front().first;
    }
};