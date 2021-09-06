class Solution {
    public List<String> ambiguousCoordinates(String s) {
        String digits = s.substring(1,s.length()-1);
        List<String> ans = new ArrayList<>();
        
        for(int i = 1; i < digits.length(); i++) {
            String x = digits.substring(0,i);
            String y = digits.substring(i);
            List<String> valid_x = valid(x);
            List<String> valid_y = valid(y);
            
            for(int j = 0; j < valid_x.size(); j++) {
                for(int k = 0; k < valid_y.size(); k++) {
                    String coor = "("+valid_x.get(j)+", "+valid_y.get(k)+")";
                    ans.add(coor);
                }
            }
        }
        
        return ans;
    }
    
    public List<String> valid(String s) {
        List<String> ans = new ArrayList<>();

        for(int i = 1; i <= s.length(); i++) {
            String p1 = s.substring(0,i);
            String p2 = s.substring(i);
            if((p1.length()==1) || (p1.length() > 1 && !p1.startsWith("0"))) {
                if((p2.length() == 0) || p2.charAt(p2.length()-1) != '0') {
                    String num = p1 + (p2.length() > 0? "."+p2 : "");
                    ans.add(num);
                }
            }
        }
        return ans;
    }
}