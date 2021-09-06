class Solution {
public:
    struct seq
    {
        int pos;
        int speed;
        int step;
    };
    int racecar(int target) {
        seq cur,temp;
        queue<seq> q;
        bool found = false;
        unordered_map<int,vector<int>> used;
        
        if(target==0)
            return 0;
        
        cur.pos = 0;
        cur.speed = 1;
        cur.step = 0;
        q.push(cur);
        used[0].push_back(1);
        while(!q.empty())
        {
            cur = q.front();
            q.pop();
            
            //A
            found = false;
            temp.pos = cur.pos+cur.speed;
            temp.speed = cur.speed*2;
            temp.step = cur.step+1;
            
            if(temp.pos==target)
            {
                return temp.step;
            }
            for(int i = 0;i<used[temp.pos].size();i++)
            {
                if(used[temp.pos][i]==temp.speed)
                {
                    found = true;
                    break;
                }
            }
            if(!found)
            {
                used[temp.pos].push_back(temp.speed);
                if(target*temp.pos<0&&temp.speed*temp.pos>0)
                    continue;
                q.push(temp);
            }
            
            //R
            found = false;
            temp.pos = cur.pos;
            temp.speed = cur.speed>0?-1:1;
            temp.step = cur.step+1;
            
            for(int i = 0;i<used[temp.pos].size();i++)
            {
                if(used[temp.pos][i]==temp.speed)
                {
                    found = true;
                    break;
                }
            }
            if(!found)
            {
                used[temp.pos].push_back(temp.speed);
                if(target*temp.pos<0&&temp.speed*temp.pos>0)
                    continue;
                q.push(temp);
            }
        }
    }
};