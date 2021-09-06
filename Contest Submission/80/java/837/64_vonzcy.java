class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        String para = paragraph.replaceAll("[!?',;.]", "");
        String[] words = para.split(" ");
        System.out.println(Arrays.toString(words));
        Map<String, Integer> map = new HashMap<>();
        for (String w : words) {
            String key = w.toLowerCase();
            map.put(key, map.getOrDefault(key, 0) + 1);
        }
        Set<String> ban = new HashSet<>();
        for (String b : banned) {
            ban.add(b);
        }
        int max = 0;
        String word = "";
        for (String key : map.keySet()) {
            if (!ban.contains(key) && map.get(key) > max) {
                max = map.get(key);
                word = key;
            }
        }
        return word;
    }
}