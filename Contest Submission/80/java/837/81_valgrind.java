class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> bannedSet = new HashSet<>();
        for(String word : banned){
            bannedSet.add(word);
        }
        Map<String, Integer> wordFreq = new HashMap<>();
        String[] splitWords = paragraph.split(" ");
        int max = 0;
        String maxWord = "";
        for(String word : splitWords){
            word = word.toLowerCase();
            int start = 0;
            int end = word.length() - 1;
            for(int i = 0; i < word.length(); i++){
                if(Character.isLetter(word.charAt(i))){
                    start = i;
                    break;
                }
            }
            for(int i = word.length() - 1; i >= 0; i--){
                if(Character.isLetter(word.charAt(i))){
                    end = i;
                    break;
                }
            }
            word = word.substring(start, end + 1);
            if(bannedSet.contains(word)) continue;
            int freq = wordFreq.getOrDefault(word, 0) + 1;
            wordFreq.put(word, freq);
            if(freq > max){
                max = freq;
                maxWord = word;
            }
        }
        return maxWord;
    }
}