class Solution {
    public int maxProfit(int[] prices) {
        int size = prices.length;
        int rightMax = prices[size - 1];

        int profit = 0;
        int pointer = size - 2;

        while (pointer > -1) {
            int curr = prices[pointer];
            if(curr > rightMax) {
                rightMax = curr;
            } else {
                profit = Math.max(profit, rightMax - curr);
            }
            pointer--;
        }
        return profit;
    }
}
