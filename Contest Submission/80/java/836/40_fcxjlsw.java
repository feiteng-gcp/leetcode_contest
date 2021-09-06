class Solution {
    public int racecar(int target) {
        int[][] dp = new int[10001][2];
        Map<Integer, Integer> map = new HashMap<>();
        Queue<Integer> q = new LinkedList<>();
        int p = 1;
        int i = 1;
        for(int j=0;j<10001;j++) {
            Arrays.fill(dp[j], 100);
        }
        while(p<10000) {
            dp[p][0] = i;
            q.offer(p);
            map.put(p, i);
            p = (p<<1)+1;
            i++;
        }
        while(!q.isEmpty()) {
            int cur = q.poll();
            for(int pos : map.keySet()) {
                if(cur+pos<=10000) {
                    int tmp = Math.min(dp[cur][0]+map.get(pos)+2, dp[cur][1]+map.get(pos)+1);
                    if(dp[cur+pos][0]>tmp){
                        dp[cur+pos][0] = tmp;
                        q.offer(cur+pos);
                    }
                }
                if(cur>pos) {
                    int tmp = Math.min(dp[cur][1]+map.get(pos)+2, dp[cur][0]+map.get(pos)+1);
                    if(dp[cur-pos][1]>tmp) {
                        dp[cur-pos][1] = tmp;
                        q.offer(cur-pos);
                    }
                }
            }
        }
        return Math.min(dp[target][0], dp[target][1]);
    }
}