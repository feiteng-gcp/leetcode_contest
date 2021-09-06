inline int sub(int dir, int spd, int pos){
    return dir*1048576+spd*65536+pos+32768;
}

const int N=2100000;
bool vis[N];

class Solution {
public:
    int racecar(int target) {
        queue<pair<int,int>> q;
        fill(vis,vis+N,false);
        q.push({sub(0,0,0),0});
        vis[sub(0,0,0)]=true;
        while(!q.empty()){
            pair<int,int> p=q.front();
            q.pop();
            int code=p.first,len=p.second;
            int dir=code/1048576,spd=code%1048576/65536,pos=code%65536-32768;
            //cout<<dir<<' '<<pos<<' '<<spd<<endl;
            int rev=sub(1-dir,0,pos);
            if(!vis[rev]){
                vis[rev]=true;
                q.push({rev,len+1});
            }
            int newpos=pos+(dir==0?1:-1)*(1<<spd);
            if(newpos==target)return len+1;
            if(spd<15&&abs(newpos)<32768){
                int acc=sub(dir,spd+1,newpos);
                if(!vis[acc]){
                    vis[acc]=true;
                    q.push({acc,len+1});
                }
            }
        }
    }
};