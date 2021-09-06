class Solution {
   boolean isLetter(char ch) {
        return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z');
    }

    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> ban = new HashSet<>();
        for (int i = 0; i < banned.length; i++) {
            ban.add(banned[i]);
        }
        
        String res = "";
        int resCount = 0;
        int i = 0;
        Map<String, Integer> count = new HashMap<>();
        while (i < paragraph.length()) {
            while (i < paragraph.length()) {
                char ch = paragraph.charAt(i);
                if (!isLetter(ch)) {
                    i++;
                } else {
                    break;
                }
            }
            int j = i;
            while (j < paragraph.length() && isLetter(paragraph.charAt(j))) {
                j++;
            }
            
            String s = paragraph.substring(i, j).trim().toLowerCase();
            if (s.length() == 0) {
                break;
            }
            
            if (!ban.contains(s)) {
                count.put(s, count.getOrDefault(s, 0) + 1);
                if (count.get(s) > resCount) {
                    res = s;
                    resCount = count.get(s);
                }
            }
            
            i = j;
        }
        return res;
    }

}