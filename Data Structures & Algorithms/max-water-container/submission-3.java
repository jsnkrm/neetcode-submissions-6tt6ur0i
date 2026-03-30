class Solution {
    public int maxArea(int[] heights) {
        int l = 0, r = heights.length - 1;
        int max = 0;
        int curr;
        while (l < r) {
            curr = (r - l) * Math.min(heights[l], heights[r]);
            if(curr > max) max = curr;
            if(heights[l] < heights[r]) {
                l++;
                continue;
            } else {
                r--;
                continue;
            }
        }
        return max;
    }
}
