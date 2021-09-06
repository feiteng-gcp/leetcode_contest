class Solution {
public:
    int racecar(int target) {
        map<pair<int, int>, int> used;
        used[make_pair(0, 1)] = 0;
        queue<pair<int, int>> wait_list;
        wait_list.push(make_pair(0, 1));
        while (!wait_list.empty()) {
            auto cur = wait_list.front();
            wait_list.pop();
            int pos = cur.first, speed = cur.second, step = used[cur];
            if (abs(speed) > target * 2) { continue; }
            pos += speed;
            speed += speed;
            if (pos == target) { return step + 1; }
            if (used.find(make_pair(pos, speed)) == used.end()) {
                used[make_pair(pos, speed)] = step + 1;
                wait_list.push(make_pair(pos, speed));
            }
            pos = cur.first;
            speed = (cur.second > 0) ? -1 : 1;
            if (used.find(make_pair(pos, speed)) == used.end()) {
                used[make_pair(pos, speed)] = step + 1;
                wait_list.push(make_pair(pos, speed));
            }
        }
    }
};