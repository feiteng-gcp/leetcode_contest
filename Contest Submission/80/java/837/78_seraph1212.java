class Solution {
    public String handle(String s) {
        s = s.toLowerCase();
        StringBuilder ans = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (ch >= 'a' && ch <= 'z') ans.append(ch);
        }
        return ans.toString();
    }
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> ban = new HashSet<>(Arrays.asList(banned));
        Map<String, Integer> cc = new HashMap<>();
        String[] ws = paragraph.split(" ");
        int freq = 0;
        String word = "";
        for (String ww : ws) {
            String w = handle(ww);
            if (w.length() == 0) continue;
            if (ban.contains(w)) continue;
            int f = cc.getOrDefault(w, 0) + 1;
            if (f > freq) {
                freq = f;
                word = w;
            }
            cc.put(w, f);
        }
        return word;
    }
}