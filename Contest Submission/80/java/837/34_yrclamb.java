class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
    	Map<String, Integer> ansMap = new HashMap<String, Integer>();
    	Set<String> bannedWords = new HashSet<String>();
    	String ansWord = "";
    	int currentMax = -1;
    	
    	for(String word : banned) bannedWords.add(word);
    	for(String word : paragraph.split(" ", -1)) {
    		word = word.replaceAll("[!?',;.]", "");
    		word = word.toLowerCase();
    		//System.out.println(word);
    		if(!bannedWords.contains(word)) {
    			int count = 1;
    			if(ansMap.containsKey(word)) count = ansMap.get(word) + 1;
    			ansMap.put(word, count);
    			if(count > currentMax) {
    				currentMax = count;
    				ansWord = word;
    			}
    		}
    	}
    	return ansWord;
    }
    
}