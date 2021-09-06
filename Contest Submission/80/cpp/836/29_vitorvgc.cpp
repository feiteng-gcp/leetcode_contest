#define MAXP 100100
#define MAXS 50
int dist[MAXP][MAXS];

class Solution {
public:
    
    typedef pair<int,int> pii;
    
    inline int pos(int p) { return p + (MAXP >> 1); }
    inline int spd(int s) { return s + (MAXS >> 1); }
    
    inline bool inside(pii p) {
        return pos(p.first) >= 0 && pos(p.first) < MAXP && spd(p.second) >= 0 && spd(p.second) < MAXS;
    }
    
    int racecar(int target) {
        
        memset(dist, -1, sizeof dist);
        queue<pii> q;
        q.push(pii(0, 1));
        dist[pos(0)][spd(1)] = 0;
        int ans = -1;
        while(!q.empty()) {
            
            pii v = q.front(); q.pop();
            
            int p = v.first;
            int s = v.second;
            int d = dist[pos(p)][spd(s)];
            
            if(p == target) {
                ans = d;
                break;
            }
            
            vector<pii> next(2);
            int sign = s > 0 ? 1 : -1;
            next[0] = pii(p + sign * (1 << (abs(s)-1)), s + sign);
            next[1] = pii(p, -sign);
            
            for(auto w : next)
                if(inside(w) && dist[pos(w.first)][spd(w.second)] == -1) {
                    q.push(w);
                    dist[pos(w.first)][spd(w.second)] = d + 1;
                }
        }
        
        return ans;
    }
};