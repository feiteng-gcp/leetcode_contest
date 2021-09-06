const int N = 21e3, M = 33, O = 16, INF = 0x3f3f3f3f;

int dis[N][M];

class Solution {
public:
  int racecar(int n) {
    int s = 0;
    static queue<int> q;
    static bool inq[N][M] = {false};
    memset(dis, 0x3f, sizeof(dis)), dis[s][O] = 0;
    inq[s][O] = true;
    for(q.push(s), q.push(O); !q.empty(); ) {
      int v, u = q.front(); q.pop();
      int y, x = q.front(); q.pop();
      inq[u][x] = false;

      if(x >= O) {
        y = O-1;
      } else {
        y = O;
      }
      v = u;
      if(dis[v][y] > dis[u][x]+1) {
        dis[v][y] = dis[u][x]+1;
        if(!inq[v][y]) {
          inq[v][y] = true;
          q.push(v);
          q.push(y);
        }
      }

      int speed;
      if(x >= O) {
        speed = 1 << x-O;
        y = x+1;
      } else {
        speed = -(1<<O-1-x);
        y = x-1;
      }
      v = u+speed;
      if(y < 0 || y >= M || v < 0 || v >= n*2+10) continue;
      if(dis[v][y] > dis[u][x]+1) {
        dis[v][y] = dis[u][x]+1;
        if(!inq[v][y]) {
          inq[v][y] = true;
          q.push(v);
          q.push(y);
        }
      }
    }
    int ans = INF;
    for(int i = 0; i < M; i++) ans = min(ans, dis[n][i]);
    return ans;
  }
};