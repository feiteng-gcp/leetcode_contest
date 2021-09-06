import java.util.*;
import java.util.stream.*;
import java.math.*;

public class Solution {


    public String mostCommonWord(String paragraph, String[] banned) {
        int maxCnt = 0;
        Set<String> banSet = new HashSet<>();
        for (String ban : banned) {
            banSet.add(ban);
        }

        Map<String, Integer> map = new HashMap<>();
        for (String token : paragraph.split("[!?',;. ]")) {
            String lower = token.toLowerCase().trim();
            if (lower.length() == 0) {
                continue;
            }
           
            if (!banSet.contains(lower)) {
                map.put(lower, map.getOrDefault(lower, 0) + 1);
                maxCnt = Math.max(maxCnt, map.get(lower));
            }
        }

        for (String s : map.keySet()) {
            if (map.get(s) == maxCnt) {
                return s;
            }
        }
        throw new RuntimeException("...");
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

    }
}
