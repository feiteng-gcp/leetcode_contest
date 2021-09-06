int f[40005][16][2];
int S[100];
//15 16000

struct node {
    int pos, s, dir;
    node(int pos = 0, int s = 0, int dir = 0) : pos(pos), s(s), dir(dir) {}
};

class Solution {
public:
    
    int INF = 10000000;
    int T = 0;
    
    int H(int a) {
        int base = 20000;
        return a += base;
    }
    
    int check(int pos, int s) {
        if (pos < 0 || pos > 40000) return 0;
        if (s > 16 || s < 0) return 0;
        return 1;
    }
    
    int racecar(int target) {
        T = H(target);
        S[0] = 1;
        for (int i = 1; i < 20; i++) S[i] = S[i-1] * 2;
        
        for (int i = 0; i <= 40000; i++) {
            for (int j = 0; j < 16; j++) {
                f[i][j][0] = f[i][j][1] = INF;
            }
        }
        
        
        f[H(0)][0][0] = 0;
        queue<node> q;
        q.push(node(H(0), 0, 0));
        
        int ans = INF;
        while(!q.empty()) {
            node now = q.front();
            q.pop();
            
            if (now.pos == T) {
                ans = f[now.pos][now.s][now.dir];
                break;
            }
            
            int tpos = 0;
            if (now.dir == 0) {
                tpos = now.pos + S[now.s];
            }
            else {
                tpos = now.pos - S[now.s];
            }
            
            int ts = now.s + 1;
            int tdir = now.dir;
            
            if (check(tpos, ts) && f[tpos][ts][tdir] == INF) {
                f[tpos][ts][tdir] = f[now.pos][now.s][now.dir] + 1;
                q.push(node(tpos, ts, tdir));
            }
            
            tpos = now.pos;
            ts = 0;
            tdir = 1 ^ now.dir;
            if (f[tpos][ts][tdir] == INF) {
                f[tpos][ts][tdir] = f[now.pos][now.s][now.dir] + 1;
                q.push(node(tpos, ts, tdir));
            }
        }
         
        return ans;
        
    }
};