class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();
        for(String str : strs){
            int[] counts = new int[26];

            for(char c : str.toCharArray()){
                counts[c-'a']++;
            }
            StringBuilder key = new StringBuilder();
            for (int value : counts){
                key.append(value+"#");
            }
            groups.computeIfAbsent(key.toString(),k-> new ArrayList<>()).add(str);
        }
        return new ArrayList<>(groups.values());
    }  
}
