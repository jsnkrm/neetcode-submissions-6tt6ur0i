class Solution {
    public int[] productExceptSelf(int[] nums) {
        int size = nums.length;
        int[] res = new int[size];
        int tot = 1;
        int hasZero = 0;
        for (int num : nums) {
            if(num == 0) {
                hasZero++;
                continue;
            } 
            tot *= num;
        }
        if(hasZero == size) tot = 0;

        if (hasZero > 1) {
            return new int[nums.length];
        }

        for (int i = 0; i < size; i++) {
            if(hasZero > 0) {
                if (nums[i] == 0) {
                    res[i] = tot;
                } else {
                    res[i] = 0;
                }
            }
            else {
                res[i] = tot / nums[i];
            }
        }        
        return res;
    }
}  
