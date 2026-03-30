class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) return 0;
        int i = 0 , j = 1;
        int size = s.length();
        Set<Character> seen = new HashSet<>();
        int ans = 1;
        seen.add(s.charAt(i));
        while ( j < size ) {
            char curr = s.charAt(j);
            if(seen.contains(curr)) {
                while(i < j) {
                    if(s.charAt(i) == curr) {
                        i++;
                        break;
                    } else {
                        seen.remove(s.charAt(i));
                        i++;                        
                    }
                }
            } else {
                ans = Math.max(ans, j - i + 1);
                seen.add(curr); 
            }
            j++;
        }
        return ans;
    }
}
