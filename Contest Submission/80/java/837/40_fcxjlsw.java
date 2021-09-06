class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        String[] words = paragraph.split(" ");
        Map<String, Integer> map = new HashMap<>();
        Set<String> bannedString = new HashSet<>();
        for(String st : banned) {
            bannedString.add(st);
        }
        int max = 0;
        String res = "";
        for(String word : words) {
            int start = 0;
            while(start<word.length() && !Character.isLetter(word.charAt(start))) start++;
            int end = word.length()-1;
            while(end>0 && !Character.isLetter(word.charAt(end))) end--;
            String tmp = word.substring(start, end+1).toLowerCase();
            if(!bannedString.contains(tmp)) {
                int count = map.getOrDefault(tmp, 0)+1;
                map.put(tmp, count);
                if(count > max) {
                    max = count;
                    res = tmp;
                }
            }
        }
        return res;
    }
}