class Solution {
    public List<String> ambiguousCoordinates(String S) {
        S = S.substring(1, S.length() - 1);
        
        List<String> res = new ArrayList<>();
        
        for (int i = 0; i + 1 < S.length(); i++) {
            List<String> A = show(S.substring(0, i + 1));
            List<String> B = show(S.substring(i + 1));
            for (String a : A) {
                for (String b : B) {
                    res.add("(" + a + ", " + b + ")");
                }
            }
        }
        
        return res;
    }
    
    private List<String> show(String s) {
        List<String> l = new ArrayList<>();
        
        if (s.length() == 1) {
            l.add(s);
            return l;
        }
        
        if (s.charAt(0) != '0') {
            l.add(s);
        }
        
        for (int i = 0; i + 1 < s.length(); i++) {
            String a = s.substring(0, i + 1);
            String b = s.substring(i + 1);
            if ((a.charAt(0) != '0' || a.length() == 1) && b.charAt(b.length() - 1) != '0') {
                l.add(a + "." + b);
            }
        }
        
        return l;
    }
}