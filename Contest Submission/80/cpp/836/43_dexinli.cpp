class Solution {
public:
    bool addA(pair<int,int> x,int target,set<pair<int,int>> &table,int cur) {
        if(x.first>0 && x.second>target) {
            return false;
        }
        auto t = make_pair(x.first*2,x.second+x.first);
        if(table.count(t)!=0) {
            return false;
        }
        table.insert(t);
        return true;
    }
    bool addR(pair<int,int> x,int target,set<pair<int,int>> &table,int cur) {
        if(x.first<-target && x.second<target) {
            return false;
        }
        auto t = make_pair(x.first>0?-1:1,x.second);
        if(table.count(t)!=0) {
            return false;
        }
        table.insert(t);
        return true;
    }
    int racecar(int target) {
        set<pair<int,int>> table;
        pair<int,int> x(1,0);
        queue<pair<int,int>> q;
        auto q1 = q;
        q.push(x);
        int cur = 0;
        while(!q.empty()) {
            while(!q.empty()) {
                auto t = q.front();
                q.pop();
                if(t.second==target) {
                    return cur;
                }
                auto t1 = make_pair(t.first*2,t.second+t.first);
                if(addA(t,target,table,cur)) {
                    q1.push(t1);
                }
                t1 = make_pair(t.first>0?-1:1,t.second);
                if(addR(t,target,table,cur)) {
                q1.push(t1);
                }
            }
            cur+=1;
            q.swap(q1);
        }
        return -1;
    }
};