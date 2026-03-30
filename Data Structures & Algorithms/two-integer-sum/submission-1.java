class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        Map<Integer, Integer> found = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            if(found.containsKey(target-nums[i])) {
                if(found.get(target-nums[i]) > i){
                    result[0] = i;
                    result[1] = found.get(target-nums[i]);
                } else {
                    result[0] = found.get(target-nums[i]);
                    result[1] = i;
                }
                break;
            } 
            found.put(nums[i], i);
        }
        return result;
    }
}
