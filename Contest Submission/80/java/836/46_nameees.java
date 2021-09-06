import java.util.*;

class Solution {

    class State {
        int timeSpent;
        int curLocation;
        int curSpeed;
        public State(int ts, int cl, int cs) {
            timeSpent = ts;
            curLocation = cl;
            curSpeed = cs;
        }
    }

    int THE_SIZE = 10000 + 1;

    int[] resultTime = new int[10000 + 1];

    // to prevent duplicate reverse operation 
    // [0] is + to -1, [1] is - to +1
    boolean[][] reversedAt = new boolean[10000 + 1][2];
    boolean[][] NEGATIVEreversedAt = new boolean[10000 + 1][2];

    Queue<State> queue = new ArrayDeque<>();

    boolean firstRun = true;

    int count = 1; // completed point 0 only

    public int racecar(int target) {
        if (firstRun) {
            solve(target);
            firstRun = false;
        }
        return resultTime[target]; // index 1 to 10000
    }

    private void solve(int target) {
        queue.add(new State(0, 0, 1));
        
        while (queue.size() > 0) {
            State cur = queue.remove();

            // take 'A'
            int ats = cur.timeSpent + 1;
            int acl = cur.curLocation + cur.curSpeed;
            int acs = cur.curSpeed * 2;
            // overflow?
            // record result
            if (acl > 0 && acl < THE_SIZE && resultTime[acl] == 0) {
                resultTime[acl] = ats;
                count++;
                // check terminate condition
                if (count == THE_SIZE) {
                    return;
                }

            }
            if (acl < THE_SIZE && acl > -THE_SIZE) {
                queue.add(new State(ats, acl, acs));
            }
            

            // take 'R'
            if (cur.curLocation < THE_SIZE && cur.curLocation > -THE_SIZE) {
                if (cur.curLocation > 0) {
                    if (cur.curSpeed > 0) {
                        if (reversedAt[cur.curLocation][0]) {
                            continue;
                        }
                        else {
                            reversedAt[cur.curLocation][0] = true;
                        }
                    }
                    else {
                        if (reversedAt[cur.curLocation][1]) {
                            continue;
                        }
                        else {
                            reversedAt[cur.curLocation][1] = true;
                        }
                    }                
                }
                else {
                    if (cur.curSpeed > 0) {
                        if (NEGATIVEreversedAt[-cur.curLocation][0]) {
                            continue;
                        }
                        else {
                            NEGATIVEreversedAt[-cur.curLocation][0] = true;
                        }
                    }
                    else {
                        if (NEGATIVEreversedAt[-cur.curLocation][1]) {
                            continue;
                        }
                        else {
                            NEGATIVEreversedAt[-cur.curLocation][1] = true;
                        }
                    }       
                }
            }
            

            int rts = cur.timeSpent + 1;
            int rcl = cur.curLocation;
            int rcs = cur.curSpeed > 0 ? -1 : 1;
            if (rcl > 0 && rcl < THE_SIZE && resultTime[rcl] == 0) {
                resultTime[rcl] = rcl;
                count++;
                // check terminate condition
                if (count == THE_SIZE) {
                    return;
                }
            }
            if (rcl > -THE_SIZE && rcl < THE_SIZE) {
                queue.add(new State(rts, rcl, rcs));
            }
            


            if (acl == target || rcl == target) {
                return;
            }
        }
    }
}

