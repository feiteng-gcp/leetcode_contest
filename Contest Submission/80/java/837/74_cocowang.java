class Solution {
    public String mostCommonWord(String p, String[] banned) {
        Set<String> set=new HashSet<>();
        String res="";
        for(String s: banned) set.add(s);
        Map<String, Integer> map=new HashMap<>();
        int max=0;
        int i=0, l=p.length();
        while(i<l){
            char c=p.charAt(i);
            if(isL(c)){
                int j=i+1;
                while(j<l&&isL(p.charAt(j))) j++;
                String tmp=p.substring(i, j).toLowerCase();
                i=j;
                if(!set.contains(tmp)){
                    map.put(tmp, map.getOrDefault(tmp, 0)+1);
                    if(map.get(tmp)>max){
                        res=tmp;
                        max=map.get(tmp);
                    }
                }
            }
            else{
                i++;
            }
        }
        
        return res;
    }
    
    public boolean isL(char c){
        return c>='A'&&c<='Z'||c>='a'&&c<='z';
    }
}