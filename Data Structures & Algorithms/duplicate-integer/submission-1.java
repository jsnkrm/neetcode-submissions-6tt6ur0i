class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> foundAlready = new HashSet<>();
        for (int n : nums) {
            if(foundAlready.contains(n)) {
                return true;
            }
            foundAlready.add(n);
        }
        return false;
    }
}