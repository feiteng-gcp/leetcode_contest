class Solution {
    public int racecar(int target) {
        IntMap[] dp = new IntMap[(target << 2) + 3];
        for (int i = 0; i < dp.length; ++i) {
            dp[i] = new IntMap();
        }
        int ZERO = (target << 1) + 1;
        Queue<Integer> pq = new ArrayDeque<Integer>();
        Queue<Integer> sq = new ArrayDeque<Integer>();
        Queue<Integer> mq = new ArrayDeque<Integer>();
        pq.offer(ZERO);
        sq.offer(1);
        mq.offer(0);
        dp[ZERO].put(1, 0);
        while (!pq.isEmpty()) {
            int p = pq.poll();
            int s = sq.poll();
            int m = mq.poll();
            // System.out.format("pos = %d, speed = %d, moves = %d\n", p - ZERO, s, m);
            if (p + s - ZERO == target) {
                return m + 1;
            }
            // A
            // if (p + s < 0 || p + s >= dp.length) {
            //     System.out.format("  skipped: %d\n", p + s);
            // }
            
            // if (p + s >= 0 && p + s < dp.length) {
            //     System.out.println("  " + dp[p + s].get(s << 1));
            // }
            if (p + s >= 0 && p + s < dp.length && !dp[p + s].containsKey(s << 1)) {
                // System.out.format("  A\n");
                pq.offer(p + s);
                sq.offer(s << 1);
                mq.offer(m + 1);
                dp[p + s].put(s << 1, m + 1);
            }
            // R
            if (s > 0) {
                if (!dp[p].containsKey(-1)) {
                    pq.offer(p);
                    sq.offer(-1);
                    mq.offer(m + 1);
                    dp[p].put(-1, m + 1);
                }
            } else {
                if (!dp[p].containsKey(1)) {
                    pq.offer(p);
                    sq.offer(1);
                    mq.offer(m + 1);
                    dp[p].put(1, m + 1);
                }
            }
        }
        return -1;
    }
    
    public static class IntMap extends HashMap<Integer, Integer> {}
}