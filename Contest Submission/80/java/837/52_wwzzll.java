class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        String newp = paragraph.replace('!', ' ')
            .replace('?', ' ')
            .replace('\'', ' ')
            .replace(',', ' ')
            .replace(';', ' ')
            .replace('.', ' ');
        String[] subp = newp.split(" ");
        HashSet<String> bans = new HashSet();
        for (String ban : banned) {
            bans.add(ban.toLowerCase());
        }
        int curMax = 0;
        String result = "";
        HashMap<String, Integer> times = new HashMap();
        for (String p : subp) {
            if (p.length() == 0) continue;
            String pLow = p.toLowerCase();
            if (bans.contains(pLow)) {
                continue;
            }
            if (times.containsKey(pLow)) {
                times.put(pLow, times.get(pLow) + 1);
            } else {
                times.put(pLow, 1);
            }
            if (times.get(pLow) > curMax) {
                curMax = times.get(pLow);
                result = pLow;
            }
        }
        return result;
    }
}