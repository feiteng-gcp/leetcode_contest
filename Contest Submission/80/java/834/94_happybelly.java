class Solution {
   
    boolean allZeros(String s) {
        for (char c : s.toCharArray())
            if (c != '0') return false;
        return true;
    }
    boolean hasLeadingZero(String s) {
        return s.charAt(0) == '0';
    }
    boolean hasTrailingZero(String s) {
        return s.charAt(s.length() -1) == '0';
    }

    List<String> gen(String x) {
        List<String> ans = new ArrayList<>();
        Set<String> set = new HashSet<>();
        if (x.length() == 1) {
            ans.add(x);
            return ans;
        }
        if (allZeros(x)) return ans;
        if (!hasLeadingZero(x)) ans.add(x);
        for (int i = 1; i < x.length(); i++) {
            String d = x.substring(0, i), f = x.substring(i);
            if (hasTrailingZero(f)) continue;
            if (d.length() > 1 && hasLeadingZero(d)) continue;
            String z = d + "." + f;
            if (!set.contains(z)) {
                ans.add(z);
                set.add(z);
            }
        }
        return ans;
    }

    public List<String> ambiguousCoordinates(String S) {
        S = S.substring(1, S.length() - 1);
        List<String> ans = new ArrayList<>();
        Set<String> has = new HashSet<>();
        for (int i = 1; i < S.length(); i++) {
            String x = S.substring(0, i), y = S.substring(i);
            List<String> sx = gen(x), sy = gen(y);
            if (!sx.isEmpty() && !sy.isEmpty()) {
                for (String xx : sx)
                    for (String yy  : sy) {
                        String z = "(" + xx + ", " + yy + ")";
                        if (!has.contains(z)) {
                            ans.add(z);
                            has.add(z);
                        }
                    }
            }
        }
        return ans;
    }
}