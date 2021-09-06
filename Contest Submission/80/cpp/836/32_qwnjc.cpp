class Solution {
public:
    int racecar(int target) {
        if (target == 0) {
            return 0;
        }
        
        queue<pair<int,int>> q;
        q.emplace(0, 1);
        set<pair<int,int>> visited;
        visited.emplace(q.front());
        int res = 0;
        int limit = 2048 * 4;
        while (!q.empty()) {
            int n = q.size();
            for (int i = 0; i < n; ++i) {
                auto p = q.front();
                q.pop();
                if (p.first + p.second == target) {
                    return res + 1;
                }
                
                if (abs(p.second) >= limit) {
                    continue;
                }
                pair<int,int> np = {p.first + p.second, p.second << 1};
                if (visited.count(np) > 0) {
                    continue;
                }
                q.emplace(np);
                visited.emplace(np);
                np.first = p.first;
                np.second = p.second > 0 ? -1 : 1;
                if (visited.count(np) > 0) {
                    continue;
                }
                q.emplace(np);
                visited.emplace(np);
            }
            ++res;
        }
        
        return 32;
    }
};