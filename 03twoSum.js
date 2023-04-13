/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
};
/*  USING HASH SET IN ONE PASS O(N)
var twoSum = function(nums, target) {
    const set = new Set()
    for ( let i in nums) {
        if (set.has(target - nums[i])) return [i, nums.indexOf(target - nums[i])]
        set.add(nums[i])
    }
};
*/
/* BRUTE FORCE O(N^2)
var twoSum = function(nums, target) {
    for (let i = 0; i< nums.length; i++) {
        for (let j = i+1; j< nums.length; j++) {
            if((nums[i]+nums[j])==target) {
                return [i,j]
            }
        }
    }
}; 
 */
