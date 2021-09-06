class Solution {
    public List<String> ambiguousCoordinates(String S) {
        List<String> result = new ArrayList<>();
        S = S.substring(1, S.length() - 1);
        for (int i = 1; i < S.length(); i++) {
            List<String> firstNum = getCord(S.substring(0, i));
            List<String> secondNum = getCord(S.substring(i, S.length()));
            for (String first : firstNum) {
                for (String second : secondNum) {
                    result.add("(" + first + ", " + second + ")");
                }
            }
        }
        return result;
    }
    private static List<String> getCord(String s) {
        List<String> result = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            String firstPart = s.substring(0, i+1);
            String secondPart = s.substring(i+1, s.length());
            if (noLeadingZero(firstPart) && noTailingZero(secondPart)) {
                String resultStr = secondPart.isEmpty() ? firstPart : firstPart + "." + secondPart;
                result.add(resultStr);
            }
        }
        return result;
    }
    private static boolean noLeadingZero(String s) {
        if (s.length() <= 1) return true;
        return s.charAt(0) != '0';
    }
    private static boolean noTailingZero(String s) {
        if (s.isEmpty()) return true;
        return s.charAt(s.length() - 1) != '0';
    }
}