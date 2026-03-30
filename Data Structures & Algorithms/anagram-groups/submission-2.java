class Solution {
    private boolean isAnagram(String s, String t) {
        int[] letters = new int[26];
        for(char c: s.toCharArray()){
            int index = (int)c - 'a';
            letters[index]++;
        }
        for(char c: t.toCharArray()){
            int index = (int)c - 'a';
            letters[index]--;
        }
        for(int i=0; i<26; i++) {
            if(letters[i]!= 0) return false;
        }
        return true;
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        for(int i = 0; i < strs.length; i++) {
            if(strs[i] != null) {
                List<String> curr = new ArrayList<>();
                curr.add(strs[i]);
                for(int j = i + 1 ; j < strs.length; j++) {
                    if(strs[j] != null && strs[j].length() == strs[i].length()) {
                        if(isAnagram(strs[i],strs[j])) {
                            curr.add(strs[j]);
                            strs[j] = null;
                        }
                    }
                }
                res.add(curr);
            }
        }
        return res;
    }
}
