typedef pair<int,int> pii;
typedef pair<int, pii> node;

class Solution {
public:
    node make_node(int a, int b, int c) {
      return make_pair(a, make_pair(b,c));
    }
    int racecar(int target) {
      priority_queue< node, vector<node>, greater<node> > q;
      set<pii> cache;
      q.push(make_node(0,0,1));
      while(!q.empty()) {
        node top = q.top();
        q.pop();
        int l = top.first;
        int d = top.second.first;
        int s = top.second.second;
        if(d==target) {
          return l;
        }
        pii state = make_pair(d,s);
        if(cache.find(state) != cache.end()) {
          continue;
        }
        //cout << l << " " << d << " " << s << endl;
        cache.insert(state);
        if(abs(d+s) > 30000) continue;
        if(cache.find(make_pair(d+s,s*2)) == cache.end()) {
          q.push(make_node(l+1, d+s, s*2));
        }
        if(s>0) {
          if(cache.find(make_pair(d,-1)) == cache.end()) {
            q.push(make_node(l+1,d,-1));
          }
        }
        else {
          if(cache.find(make_pair(d,1)) == cache.end()) {
            q.push(make_node(l+1,d,1));
          }          
        }
      }
      return 0;
    }
};