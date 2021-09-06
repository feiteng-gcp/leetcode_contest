using pii = pair<int, int>;
class Solution {
public:
    int racecar(int target) {
        queue<pair<pii, int>> que;
        que.push({{0, 1}, 0});
        set<pii> vis;
        while (que.size()) {
            auto pair = que.front();
            que.pop();
            int pos = pair.first.first, speed = pair.first.second, step = pair.second;
            if (pos == target) return step;
            if (pos > target * 2 + 10 || pos < -target * 2) {
                continue;
            }
            // cout << pos << " " << speed << " " << step << endl;
            
            // speed
            {
                
                int npos = pos + speed;
                int ns = speed * 2;
                if (vis.find({npos, ns}) == vis.end()) {
                    que.push({{npos, ns}, step + 1});
                    vis.insert({npos, ns});
                }
                
            }
            
            {
                int npos = pos;
                int ns = 0;
                if (speed > 0) {
                    ns = - 1;
                } else {
                    ns = 1;
                }
                // int ns = max(speed - 1, 1);
                if (vis.find({npos, ns}) == vis.end()) {
                    que.push({{npos, ns}, step + 1});
                    vis.insert({npos, ns});
                }
            }
        }
        return 0;
    }
};