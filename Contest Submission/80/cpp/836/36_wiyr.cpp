class Solution {
public:
    int racecar(int target) {
        map<pair<int, int>, int> dist;
        queue<pair<int, int>> Q;
        Q.push(make_pair(0, 1));
        while(!Q.empty()) {
            pair<int, int> t = Q.front();
            Q.pop();
            if (t.first == target) {
                return dist[t];
            }
            // speed up
            int np = t.first + t.second;
            int nv = t.second * 2;
            if (np <= 2*target && np >= -2*target) {
                pair<int, int> nt = make_pair(np, nv);
                if (dist.count(nt) == 0) {
                    dist[nt] = dist[t] + 1;
                    Q.push(nt);
                }
            }
            if (t.second > 0) {
                nv = -1;
                np = t.first;
                pair<int, int> nt = make_pair(np, nv);
                if (dist.count(nt) == 0) {
                    dist[nt] = dist[t] + 1;
                    Q.push(nt);
                }
            } else {
                nv = 1;
                np = t.first;
                pair<int, int> nt = make_pair(np, nv);
                if (dist.count(nt) == 0) {
                    dist[nt] = dist[t] + 1;
                    Q.push(nt);
                }
            }
        }

        return -1;
    }
};
