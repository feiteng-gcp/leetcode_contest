class Solution {
	int[][] memo = new int[30000][40];
	int ans = Integer.MAX_VALUE;
	Map<Integer, Integer> stepMap = new HashMap<Integer, Integer>();
    public int racecar(int target) {
    	stepMap.put(1, 20);
    	stepMap.put(2, 21);
    	stepMap.put(4, 22);
    	stepMap.put(8, 23);
    	stepMap.put(16, 24);
    	stepMap.put(32, 25);
    	stepMap.put(64, 26);
    	stepMap.put(128, 27);
    	stepMap.put(256, 28);
    	stepMap.put(512, 29);
    	stepMap.put(1024, 30);
    	stepMap.put(2048, 31);
    	stepMap.put(4096, 32);
    	stepMap.put(8192, 33);
    	stepMap.put(16384, 34);
    	stepMap.put(-1, 19);
    	stepMap.put(-2, 18);
    	stepMap.put(-4, 17);
    	stepMap.put(-8, 16);
    	stepMap.put(-16, 15);
    	stepMap.put(-32, 14);
    	stepMap.put(-64, 13);
    	stepMap.put(-128, 12);
    	stepMap.put(-256, 11);
    	stepMap.put(-512, 10);
    	stepMap.put(-1024, 9);
    	stepMap.put(-2048, 8);
    	stepMap.put(-4096, 7);
    	stepMap.put(-8192, 6);
    	stepMap.put(-16384, 5);
    	
        //memo[0][0+20] = 0;
        //memo[1][1+20] = 1;
        gogo(target, 0, 1, 0);
        return ans;
    }
    
    private void gogo(int target, int current, int speed, int steps) {
    	if(steps > ans) return;
    	if(current > 0 && current > target * 2) return;
    	if(current < 0 && current < target * 2) return;
    	if(memo[current][stepMap.get(speed)] == 0)
    		memo[current][stepMap.get(speed)] = steps;
    	else if(memo[current][stepMap.get(speed)] <= steps) return;
    	else memo[current][stepMap.get(speed)] = steps;
    	
    	//System.out.println(current + ", " + speed + ", " + steps + ", " + memo[current][stepMap.get(speed)]);
    	if(current == target) {
    		if(steps < ans)
    			ans = steps;
    		return;
    	}
    	
    	if(current < target && speed > 0) {
    		gogo(target, current+speed, speed*2, steps+1);
    		gogo(target, current, -1, steps+1);
    	}
    	else if(current < target && speed < 0) {
    		gogo(target, current, 1, steps+1);
    		gogo(target, current+speed, speed*2, steps+1);
    	}
    	else if(current > target && speed > 0) {
    		gogo(target, current, -1, steps+1);
    		gogo(target, current+speed, speed*2, steps+1);
    	}
    	else if(current > target && speed < 0) {
    		gogo(target, current+speed, speed*2, steps+1);
    		gogo(target, current, 1, steps+1);
    	}
    }
}