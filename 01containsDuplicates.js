/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {

};
/*  CHECK IF THEY HAVE THE SAME LENGTH, SINCE THERE ARE NO DUPLICATES IN A HASHSET
    const hashSet = new Set(nums);
    if (hashSet.size == nums.length) {
        return false;
    }
    else {
        return true;
    }
 */
/* HASHSET SOLUTION
    const hashSet = new Set();
    for (let n of nums) {
        if (hashSet.has(n)) return true;
        hashSet.add(n)
    }
    return false;

    //WRONG ONE:
    const hashSet = {};
    for (let n of nums) {
        if (hashSet[n]) {
            return true;
        }
        hashSet[n] = true;
    }
    return false;
*/

/* BRUT FORCE SOLUTION, TWO FOR LOOPS O(N^2)
var containsDuplicate = function(nums) {
    for (var i = 0; i < nums.length; i++) {
        for (var j = i+1; j < nums.length; j++) {
            if (nums[i] == nums[j]) {
                return true;
            }
        }
    }
    return false;
};
 */

 /* ANOTHER WAY TO IMPLEMENT BRUT FORCE SOLUTION, TWO FOR LOOPS O(N^2)
 var containsDuplicate = function(nums) {
    while(nums.length > 1) {
        var value = nums.pop();
        if (nums.includes(value)) {
            return true;
        }
    }
    return false;
};
  */
