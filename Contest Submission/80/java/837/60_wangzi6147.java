class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        String[] ss = paragraph.split(" ");
        Map<String, Integer> map = new HashMap<>();
        Set<String> ban = new HashSet<>();
        for (String s : banned) {
            ban.add(s.toLowerCase());
        }
        int max = Integer.MIN_VALUE;
        String result = "";
        for (String word : ss) {
            word = word.replaceAll("[!\\?',;\\.]", "");
            word = word.toLowerCase();
            if (ban.contains(word)) {
                continue;
            }
            if (!map.containsKey(word)) {
                map.put(word, 0);
            }
            map.put(word, map.get(word) + 1);
            if (map.get(word) > max) {
                max = map.get(word);
                result = word;
            }
        }
        return result;
    }
}