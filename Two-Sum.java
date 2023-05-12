class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] new_arr = {0, 0};

        for (int i = 0; i < nums.length; i++) {
            int first_num = nums[i];
            for (int j = i+1; j < nums.length; j++) {
                if (first_num + nums[j] == target) {
                    new_arr[0] = i;
                    new_arr[1] = j;
                    return new_arr;
                }
            }

            // if first number + going through array of numbers = target
        }
    return null;
    }
}
// go through each number and find its other number that has its addition as the target
