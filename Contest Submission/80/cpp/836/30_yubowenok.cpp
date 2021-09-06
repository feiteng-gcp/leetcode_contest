typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

const int INF = (int)1E9;
#define MAXN 200000
#define MID MAXN/2
int dist[2][MAXN];
struct dij {
  int x, i, d;
  dij(int _i, int _x, int _d): x(_x), i(_i), d(_d) {}
  bool operator < (const dij &ano) const {
    return d > ano.d;
  };
};

class Solution {
public:
  int racecar(int target) {
    REP(i,0,2) REP(v,0,MAXN) dist[i][v] = INF;
    dist[0][MID] = 0;
    priority_queue<dij> pq;
    pq.push(dij(0, MID, 0));
    while (pq.size()) {
      dij now = pq.top(); pq.pop();
      if (now.d > dist[now.i][now.x]) continue;
      if (now.x == target + MID) return now.d - 1;
      int nx = now.x, ni = !now.i;
      if (now.d + 1 < dist[ni][nx]) {
        dist[ni][nx] = now.d + 1;
        pq.push(dij(ni, nx, now.d + 1));
      }
      int dir = now.i == 0 ? 1 : -1;
      REP(b,0,25) {
        nx += (1<<b) * dir;
        if (nx >= MAXN || nx < 0) break;
        int cost = now.d + b + 2;
        if (cost < dist[ni][nx]) {
          dist[ni][nx] = cost;
          pq.push(dij(ni, nx, cost));
        }
      }
    }
  }
};