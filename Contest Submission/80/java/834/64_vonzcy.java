class Solution {
    public List<String> ambiguousCoordinates(String S) {
        S = S.substring(1, S.length() - 1);
        List<String> res = new ArrayList<>();
        for (int i = 1; i < S.length(); i++) {
            String first = S.substring(0, i);
            String second = S.substring(i);
            List<String> front = distribute(first);
            List<String> back = distribute(second);
            for (String f : front) {
                for (String b : back) {
                    res.add("(" + f + ", " + b + ")");
                }
            }
        }
        return res;
    }
    
    private List<String> distribute(String num) {
        List<String> res = new ArrayList<>();
        for (int i = 1; i < num.length(); i++) {
            String front = num.substring(0, i);
            String second = num.substring(i);
            if ((front.charAt(0) != '0' || front.length() == 1) 
               && !second.endsWith("0")) {
                res.add(front + "." + second);
            }    
        }
        if (num.length() > 0 && (num.charAt(0) != '0' || num.length() == 1)) {
            res.add(num);
        }
        return res;
    }
}