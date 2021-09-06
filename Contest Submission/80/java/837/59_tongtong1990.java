class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        String[] words = paragraph.split(" ");
        Set<String> bannedSet = new HashSet<>();
        for (int i = 0; i < banned.length; i++) bannedSet.add(banned[i]);
        Map<String, Integer> freq = new HashMap<>();
        int resultNum = 0;
        String result = "";
        for (int i = 0; i < words.length; i++) {
            String word = removePaun(words[i]);
            if (bannedSet.contains(word)) continue;
            if (!freq.containsKey(word)) freq.put(word, 0);
            freq.put(word, freq.get(word) + 1);
            if (freq.get(word) > resultNum) {
                resultNum = freq.get(word);
                result = word;
            }
        }
        return result;
    }
    private static String removePaun(String word) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (c == '!' || c == '?' || c == '\'' || c == ',' || c == ';' || c == '.') continue;
            c = c >= 'a' && c <= 'z' ? c : (char)(c - 'A' + 'a');
            sb.append(c);
        }
        return sb.toString();
    }
}