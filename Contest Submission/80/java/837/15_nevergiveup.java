class Solution {

	private boolean check(char ch) {
		
		if (ch >= 'a' && ch <= 'z') {
			return true;
		} else if (ch >= 'A' && ch <= 'Z') {
			return true;
		} else {
			return false;
		}
		
	}
	
	private char getChar(char ch) {
		
		if (ch >= 'a' && ch <= 'z') {
			return ch;
		} else {
			return (char) (ch - 'A' + 'a');
		}
		
	}
	
    public String mostCommonWord(String paragraph, String[] banned) {
     
    	Set<String> set = new HashSet<>();
    	for (String word : banned) {
    		set.add(word);
    	}
    	Map<String , Integer> map = new HashMap<>();
    	int i , length = paragraph.length();
    	for (i = 0;i < length;i ++) {
    		if (check(paragraph.charAt(i))) {
    			StringBuilder builder = new StringBuilder();
    			while (i < length && check(paragraph.charAt(i))) {
    				builder.append(getChar(paragraph.charAt(i)));
    				i ++;
    			}
    			String string = builder.toString();
    			if (!map.containsKey(string)) {
    				map.put(string , 1);
    			} else {
    				map.put(string , map.get(string) + 1);
    			}
    		}
    	}
    	String ans = "";
    	int max = 0;
    	for (Map.Entry<String , Integer> entry : map.entrySet()) {
    		if (!set.contains(entry.getKey())) {
    			if (entry.getValue() > max) {
    				max = entry.getValue();
    				ans = entry.getKey();
    			}
    		}
    	}
    	return ans;
    	
    }
	
}