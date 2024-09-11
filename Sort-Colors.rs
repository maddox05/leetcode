impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
    let len: usize = nums.len();
    for i in 0..len {
        let mut min_index: i32 = i as i32;
        for j in i..len {
            if (nums[j] < nums[min_index as usize]) {
                min_index = j as i32;
            }
        }
        // swap
        let tmp = nums[min_index as usize];
        nums[min_index as usize]=nums[i];
        nums[i]=tmp;

    }
}
}
