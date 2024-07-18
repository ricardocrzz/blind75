# 4.5mins
# time and space O(n) 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myset = set(nums) # time and space O(n) 
        for i in myset: #time O(n)
            if (target-i) in myset: #time O(1)
                return [nums.index(i),nums.index(target-i)]
        return False
        
