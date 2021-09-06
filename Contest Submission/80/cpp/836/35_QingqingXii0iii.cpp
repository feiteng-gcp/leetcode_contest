int dp[40050][50];
bool v[40050][50];
queue<pair<int,int> > Q;
class Solution {
public:
    int N;
    const int M = 25;
    int racecar(int target) {
        memset(dp,0x3f,sizeof(dp));
        memset(v,0,sizeof(v));
        N = min(20000 + 20,4 * target);
        dp[0 + N][1 + M] = 0;
        Q.push(make_pair(0,1));
        while(!Q.empty()){
            pair<int,int> p = Q.front();Q.pop();
            int u = p.first;
            int speed = p.second;
            //cout << u << " " << speed << endl;
            if(v[u + N][speed + M]) continue;
            v[u + N][speed + M] = 1;
            int v,s1;
            if(speed >= 0) v = u + (1 << (speed - 1)),s1 = speed + 1;
            else v = u - (1 << (-speed - 1)),s1 = speed - 1;
            if(v >= -N && v <= N){
                if(dp[v + N][s1 + M] > dp[u + N][speed + M] + 1){
                    dp[v + N][s1 + M] = dp[u + N][speed + M] + 1;
                    Q.push(make_pair(v,s1));
                }
            }
            v = u;
            if(speed >= 0) s1 = -1;
            else s1 = 1;
            if(v >= -N && v <= N){
                if(dp[v + N][s1 + M] > dp[u + N][speed + M] + 1){
                    dp[v + N][s1 + M] = dp[u + N][speed + M] + 1;
                    Q.push(make_pair(v,s1));
                }
            }
        }
        int ans = 1e9;
        for(int i = 0;i < 50;i++){
            ans = min(dp[target + N][i],ans);
        }
        return ans;
    }
};