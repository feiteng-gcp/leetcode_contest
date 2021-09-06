class Solution {
	
	private static class Element {
		public int pos;
		public int speed;
		public int direction;
		public Element(int pos , int speed , int direction) {
			this.pos = pos;
			this.speed = speed;
			this.direction = direction;
		}
	}
	
	private int getDist(int speed , int direction) {
		
		if (direction == 1) {
			return (1 << speed);
		} else {
			return - (1 << speed);
		}
		
	}
	
	private static int[][][] dists = new int[70000][20][2];
	
    public int racecar(int target) {
        
    	Queue<Element> queue = new LinkedList<>();
    	queue.add(new Element(30000 , 0 , 1));
    	for (int i = 0;i < 70000;i ++) {
    		for (int j = 0;j < 20;j ++) {
    			for (int k = 0;k < 2;k ++) {
    				dists[i][j][k] = - 1;
    			}
    		}
    	}
    	dists[30000][0][1] = 0;
    	while (!queue.isEmpty()) {
    		Element e = queue.poll();
    		int currentDist = dists[e.pos][e.speed][e.direction];
    		// speed up
    		int next = e.pos + getDist(e.speed , e.direction);
    		if (next < 70000 && next >= 0) {
    			if (next == target + 30000) {
    				return currentDist + 1;
    			}
    			if (dists[next][e.speed + 1][e.direction] < 0) {
    				dists[next][e.speed + 1][e.direction] = currentDist + 1;
    				queue.add(new Element(next , e.speed + 1 , e.direction));
    			}
    		}
    		// reverse
    		if (dists[e.pos][0][1 - e.direction] < 0) {
    			dists[e.pos][0][1 - e.direction] = currentDist + 1;
    			queue.add(new Element(e.pos , 0 , 1 - e.direction));
    		}
    	}
    	return - 1;
    	
    }
    
 
}