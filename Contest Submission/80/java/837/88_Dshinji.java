class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> banSet = new HashSet<>();
        for(String word : banned) {
            banSet.add(word.toLowerCase());
        }
        
        String[] words = paragraph.split(" ");
        Map<String,Integer> freq = new HashMap<>();
        
        for(String word : words) {
            if(!Character.isLetter(word.charAt(word.length()-1))) {
                word = word.substring(0,word.length()-1);
            }
            word = word.toLowerCase();
            if(!banSet.contains(word)) {
                int count = freq.getOrDefault(word,0);
                count++;
                freq.put(word,count);
            }
        }
        
        String ans = ""; int max = 0;
        for(String word : freq.keySet()) {
            int count = freq.get(word);
            if(count > max) {
                max = count;
                ans = word;
            }
        }
        
        return ans;
    }
}