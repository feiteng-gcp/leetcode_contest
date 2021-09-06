class Solution {
    public int racecar(int target) {
        for (int i = 0; i <= 30000; ++i)
            for (int j = 0; j < 30; ++j) {
                visited[i][j] = -1;
            }
        speed[0] = 1;
        for (int i = 1; i < speed.length; ++i)
            speed[i] = speed[i - 1] * 2;
        visited[20000][16] = 0;
        Queue<Integer> q = new LinkedList();
        q.add(20000);
        q.add(16);
        while(q.size() > 0) {
            int curPos = q.poll();
            int curSpeed = q.poll();
            int curSteps = visited[curPos][curSpeed];
            if (curPos == target + 20000) return curSteps;
            boolean positive = curSpeed > 15;
            int speedValue = positive ? speed[curSpeed - 15 - 1] : -1 * speed[14 - curSpeed];
            // A direction
            int newPos =curPos + speedValue;
            int newSpeed = positive ? curSpeed + 1 : curSpeed - 1;
            //System.out.println("New Pos:" + newPos + )
            if (newPos == target + 20000) return curSteps + 1;
            if (newPos < 0 || newPos > 40000 || newSpeed < 0 || newSpeed >= 30) {
                
            } else {
                if (visited[newPos][newSpeed] == -1) {
                    visited[newPos][newSpeed] = curSteps + 1;
                    q.add(newPos);
                    q.add(newSpeed);
                }
            }
            // R direction
            int newPosR = curPos;
            int newSpeedR = positive ? 14 : 16;
                if (visited[newPosR][newSpeedR] == -1) {
                    visited[newPosR][newSpeedR] = curSteps + 1;
                    q.add(newPosR);
                    q.add(newSpeedR);
                }
            
        }
        return -1;
    }
    
    int[] speed = new int[20];
    
    int[][] visited = new int[40001][30];
}