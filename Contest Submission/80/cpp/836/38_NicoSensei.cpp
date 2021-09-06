class Solution {
public:
    int racecar(int target) {
        if (target == 0) return 0;
        map<pair<int, int>, int> steptable;
        queue<int> posque;
        queue<int> vque;
        
        posque.push(0);
        vque.push(1);
        steptable[make_pair(0, 1)] = 0;
        while (!posque.empty()) {
            int p = posque.front();
            int v = vque.front();
            // cout << p << " " << v << endl;
            posque.pop(), vque.pop();
            
            int t = steptable[make_pair(p, v)];
            
            if (p + v == target) {
                return t + 1;
            }
            
            if (p + v <= 2 * target + 1 && p >= -target - 1) {
                auto it = steptable.find(make_pair(p + v, 2 * v));
                if (it == steptable.end()) {
                    steptable[make_pair(p + v, 2 * v)] = t + 1;
                    posque.push(p + v);
                    vque.push(2 * v);
                }
            }
            
            if (p <= 2 * target + 1 && p >= -target - 1) {
                if (v > 0) v = -1;
                else v = 1;
                
                auto it = steptable.find(make_pair(p, v));
                if (it == steptable.end()) {
                    steptable[make_pair(p, v)] = t + 1;
                    posque.push(p);
                    vque.push(v);
                }
            }
        }
        return -1;
    }
};