class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Map<String, Integer> f = new HashMap<>();
        Set<String> b = new HashSet<>();
        for (String w : banned) b.add(w);
        String s = "";
        for (int i = 0; i <= paragraph.length(); i++) {
            char c;
            if (i == paragraph.length() || !Character.isLetter(c = paragraph.charAt(i))) {
                if (!s.isEmpty() && !b.contains(s)) {
                    f.put(s, f.getOrDefault(s, 0) + 1);
                } 
                s = "";
                continue;
            } else {
                s += Character.toLowerCase(c);
            }
        }
        int max = 0; 
        String ans = "";
        for (Map.Entry<String, Integer> e : f.entrySet()) {
            s = e.getKey(); int v = e.getValue();
            if (v > max) {
                max = v;
                ans = s;
            }
        }
        return ans;
    }
}