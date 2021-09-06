class Solution {
public:
    typedef pair<int, int> pii;
typedef priority_queue<pii, vector<pii>, greater<pii> > pqpii;

bool updateQ(pqpii& q, pqpii& aq, pqpii& bq, vector<int>& dp, int isR, int target)
{
    while(!q.empty())
    {
        pii cur = q.top(); q.pop();
        if(cur.second == target) return true;
        int w = 2, st = 1;
        while(1)
        {
            int nxt = cur.second + isR * (w - 1);
            if(nxt <= 0 || nxt >= 2 * target) break;
            if(cur.first + 1 + st <= dp[nxt])
            {
                dp[nxt] = cur.first + 1 + st;
                bq.push({dp[nxt], nxt});
            }
            w <<= 1;
            st++;
        }
        
        w = 2; st = 1;
        while(1)
        {
            int nxt = cur.second - isR * (w - 1);
            if(nxt <= 0 || nxt >= 2 * target) break;
            if(cur.first + 2 + st <= dp[nxt])
            {
                dp[nxt] = cur.first + 2 + st;
                aq.push({dp[nxt], nxt});
            }
            w <<= 1;
            st++;
        }
    }
    return false;
}

int racecar(int target)
{
    vector<int> dp(2 * target, 0x3f3f3f3f);
    dp[0] = 0;
    pqpii lq, rq;
    lq.push({0, 0});
    while(!lq.empty() || !rq.empty())
    {
        pqpii tlq, trq;
        if(updateQ(lq, tlq, trq, dp, 1, target)) break;
        if(updateQ(rq, trq, tlq, dp, -1, target)) break;
        lq = tlq;
        rq = trq;
    }
    return dp[target] - 1;
}

};