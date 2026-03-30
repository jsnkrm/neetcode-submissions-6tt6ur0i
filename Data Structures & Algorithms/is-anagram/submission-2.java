class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;
        int[] letters = new int[26];
        for(char c: s.toCharArray()) {
            int index = c - 'a';
            letters[index]++;
        }
        for(char c: t.toCharArray()) {
            int index = c - 'a';
            letters[index]--;
        }
        for(int i = 0; i < 26; i++) {
            if(letters[i] != 0) return false;
        }
        return true;
    }
}
