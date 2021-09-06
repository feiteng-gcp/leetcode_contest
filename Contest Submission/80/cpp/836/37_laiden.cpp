bool solve = false;
unordered_set<string> seen;
unordered_map<int, int> at;

class Solution {
public:
    
    int racecar(int targ) {
        
        if(!solve){

        	solve = true;

            queue<pair<int,int>> q;
            int dist = 0, rel = 1;
            q.push({0, 1});
            
            while(at.size() != 10000){
                
                pair<int,int> x = q.front(); q.pop();

                int ff = x.first;
                int ss = x.second;
                
                string sig = to_string(ff) + " " +  to_string(ss);
                if(!seen.count(sig)){
                    seen.insert(sig);

                    if(ff >= 1 && ff <= 10000 && !at.count(ff)){
                        at[ff] = dist; 
                    }

                    if(abs(ff+ss) < 29000 && abs(ss*2) < 29000) q.push({ff+ss, ss*2});
                    q.push({ff, ss > 0 ? -1 : 1});
                }
                if(--rel == 0) rel = q.size(), dist++;
            }  
            
        }
        return at[targ]; 
    }
};