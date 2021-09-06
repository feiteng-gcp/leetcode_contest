class Solution {
public:
    int racecar(int target) {
        unordered_map<long long, unordered_map<long long, int>> m;
        queue<pair<pair<long long, long long>, int>> q;
        q.push(make_pair(make_pair(0, 1), 0));
        while (!q.empty()) {
            auto p = q.front();
            q.pop();
            long long u = p.first.first;
            long long v = p.first.second;
            int d = p.second;
            // cout << u << " " << v << " " << d << endl;
            
            if (m.find(u) == m.end() || m[u].find(v) == m[u].end()) {
                m[u][v] = d;
            } else {
                continue;
            }
            
            if (u == target) return d;
            if (u + v == target) return d + 1;
            if (u + v >= 0) 
                q.push(make_pair(make_pair(u + v, v << 1), d + 1));
            if (u)
                q.push(make_pair(make_pair(u, (v > 0 ? -1 : 1)), d + 1));
        }
    }
};