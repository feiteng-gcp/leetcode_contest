int visited[60001][40];
int cte=30000;
class Solution {
public:
    int racecar(int target) {
        memset(visited,-1,sizeof(visited));
        queue<pair<int,int> >Q;
        
        Q.push(make_pair(0,0));
        visited[0+cte][0+16]=0;
        int ans=-1;
        while(!Q.empty()){
            pair<int,int>P=Q.front();
            Q.pop();
            int node=P.first;
            int speed=P.second;
            //speed 0,1,2,3,4,5,6,...16
            //       -1,-2,.........-16
            if(node==target){
                ans=visited[node+cte][speed+16];
                break;
            }
            
            // A
            if(speed>=0){
                int val=1<<speed;
                if(node+val<=30000 && speed+1<=16){
                    if(visited[node+val+cte][speed+1+16]==-1){
                        visited[node+val+cte][speed+1+16]=visited[node+cte][speed+16]+1;
                        Q.push(make_pair(node+val,speed+1));
                    }
                }
            }else{
                int val=1<<(abs(speed)-1);
                if(node-val>=-30000 && speed-1>=-16){
                    if(visited[node-val+cte][speed-1+16]==-1){
                        visited[node-val+cte][speed-1+16]=visited[node+cte][speed+16]+1;
                        Q.push(make_pair(node-val,speed-1));
                    }
                }
            }
            
            // R
            if(speed>=0){
                if(visited[node+cte][-1+16]==-1){
                    visited[node+cte][-1+16]=visited[node+cte][speed+16]+1;
                    Q.push(make_pair(node,-1));
                }
            }else{
                if(visited[node+cte][0+16]==-1){
                    visited[node+cte][0+16]=visited[node+cte][speed+16]+1;
                    Q.push(make_pair(node,0));
                }
            }
            
            
        }
        
        return ans;
    }
};