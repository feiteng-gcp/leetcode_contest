typedef long long int64;
typedef pair<int64, int64> ii;
class Solution {
public:
    int racecar(int target) {
        queue<ii> Q;
        map<ii, int> visit;
        visit[{0, 1}] = 0;
        Q.push({0, 1});
        // int cnt = 0;
        while (!Q.empty()) {
            int64 x = Q.front().first;
            int64 s = Q.front().second;
            int step = visit[{x, s}];
            // if (++cnt % 10000 == 0)
            // trace(x, s, step);
            if (x == target) return step;
            Q.pop();
            // if (s <= 1LL << 60) {
            {
                int64 y = x + s;
                int64 t = s * 2;
                if (abs(y) <= target * 2 && !visit.count({y, t})) {
                    visit[{y, t}] = step + 1;
                    Q.push({y, t});
                }
            }
            int64 y = x;
            int64 t = s > 0 ? -1 : 1;
            if (abs(y) <= target * 2 && !visit.count({y, t})) {
                visit[{y, t}] = step + 1;
                Q.push({y, t});
            }
        }
        return -1;
    }
};
