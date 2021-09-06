import java.util.*;

class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        paragraph = paragraph.toLowerCase();

        paragraph = paragraph.replaceAll("[^A-Za-z ]+", "");

        String[] words = paragraph.split(" ");

        // for (String word : words) {
        //     System.out.println(word);
        // }

        HashMap<String, Integer> map = new HashMap<>();

        for (String word : words) {
            map.putIfAbsent(word, 0);
            map.put(word, map.get(word) + 1);
        }

        for (String word : banned) {
            map.remove(word);
        }

        int max = Collections.max(map.values());

        for (String word : map.keySet()) {
            if (max == map.get(word)) {
                return word;
            }
        }

        return "";
    }
}