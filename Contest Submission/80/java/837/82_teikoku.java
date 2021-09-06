class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> bSet = new HashSet<>(Arrays.asList(banned));
        Map<String, Integer> cMap = new HashMap<>();
        
        List<String> words = getWords(paragraph);
        
        for (String word : words) {
            if (bSet.contains(word)) continue;
            cMap.put(word, cMap.getOrDefault(word, 0) + 1);
        }
        
        int maxCount = 0;
        String word = null;
        for (Map.Entry<String, Integer> entry : cMap.entrySet()) {
            int count = entry.getValue();
            if (count > maxCount) {
                maxCount = count;
                word = entry.getKey();
            }
        }
        
        return word;
        
    }
    
    List<String> getWords(String p) {
        StringBuilder sb = new StringBuilder();
        List<String> words = new ArrayList<>();
        for (char c : p.toCharArray()) {
            if (c >= 'A' && c <= 'Z') c = (char)('a' + (c - 'A'));
            if (c >= 'a' && c <= 'z') {
                sb.append(c);
            } else {
                if (sb.length() > 0) {
                    words.add(sb.toString());
                    sb = new StringBuilder();
                }
            }
        }
        if (sb.length() > 0) words.add(sb.toString());
        return words;
    }
}