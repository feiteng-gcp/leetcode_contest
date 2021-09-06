class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> b = new HashSet<>();
        
        for (String ban : banned) {
            b.add(ban);
        }
        
        Map<String, Integer> m = new HashMap<>();
        int max = 0;
        String res = null;
        
        String[] words = paragraph.split("[^A-Za-z]+");
        
        for (String word : words) {
            word = word.toLowerCase();
            if (b.contains(word)) {
                continue;
            }
            int c = m.getOrDefault(word, 0) + 1;
            m.put(word, c);
            if (c > max) {
                max = c;
                res = word;
            }
        }
        
        return res;
    }
    
    private boolean isLetter(char c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
    }
}