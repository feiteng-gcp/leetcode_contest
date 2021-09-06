class Solution {
  boolean inInteger(long value, long target) {
        return value >= -target - 100 && value <= target + 100;
    }
    
//    boolean inInteger(long value) {
//        return value >= Integer.MIN_VALUE && value <= Integer.MAX_VALUE;
//    }

    public int racecar(int target) {

        Queue<long[]> q = new ArrayDeque<>();
        q.add(new long[] {0, 1});

        Map<String, Integer> dis = new HashMap<>();
        dis.put("0,1", 0);

        while (!q.isEmpty()) {
            long[] node = q.poll();
            long position = node[0];
            long speed = node[1];
            int d = dis.get(position + "," + speed);

            if (position == target) {
                //System.out.println(dis.size());
                return d;
            }

            // A
            long newP = position + speed;
            long newS = speed * 2;
            //String key = "";
            if (newP >= -100 && inInteger(newP, target) && inInteger(newS, target)) {
                String key = newP + "," + newS;
                if (!dis.containsKey(key)) {
                    dis.put(key, d + 1);
                    q.add(new long[] {newP, newS});
                }
            }

            // R
            newP = position;
            newS = speed > 0 ? -1 : 1;
            if (newP >= -100 && inInteger(newP, target) && inInteger(newS, target)) {
                String key = newP + "," + newS;
                if (!dis.containsKey(key)) {
                    dis.put(key, d + 1);
                    q.add(new long[] {newP, newS});
                }
            }
        }
        return -1;
    }

}