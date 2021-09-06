const int maxN = 100005;
const int maxK = 21;
const int mod = (int)1e9 + 7;
const int inf = (int)1e9;

int d[2 * maxN + 5][2][maxK];


class Solution {
public:
        int racecar(int target) {

        for(int i = 0; i < 2 * maxN + 5; ++i){
            for(int sign = 0; sign < 2; sign++){
                for(int k = 0; k < maxK; ++k){
                    d[i][sign][k] = inf;
                }
            }
        }
        d[0 + maxN][0][0] = 0;
        queue<int> q;
        q.push(0);
        q.push(0);
        q.push(0);
        while(!q.empty()){
            int position = q.front(); q.pop();
            int sign = q.front(); q.pop();
            int power = q.front(); q.pop();


            int val = d[position + maxN][sign][power];
            if(position == target){
                return val;
            }
            sign = (sign == 0 ? +1 : -1);
            int velocity = 1 << power;

          //  bug3(position , sign , velocity);

            int newposition = position + sign * velocity;
            int newpower = power + 1;
            int newsign = (sign == +1 ? 0 : 1);
            //bug3(newposition , newpower , newsign);

            if(newposition > -maxN && newposition < maxN)
            if(1 + val < d[newposition + maxN][newsign][newpower]){
                d[newposition + maxN][newsign][newpower] = 1 + val ;
                q.push(newposition);
                q.push(newsign);
                q.push(newpower);
            }

            newposition = position;
            newpower = 0;
            newsign = (sign == +1 ? 1 : 0);
            if(1 + val < d[newposition + maxN][newsign][newpower]){
                d[newposition + maxN][newsign][newpower] = 1 + val;
                q.push(newposition);
                q.push(newsign);
                q.push(newpower);
            }
        }
        return 0;
    }


};