class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashArr = {}

        for i in range(len(nums)):
            if (target - nums[i]) in hashArr:
                return [hashArr[target - nums[i]], i]
            
            hashArr[nums[i]] = i
        
        