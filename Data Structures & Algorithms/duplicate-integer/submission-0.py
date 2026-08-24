class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashArr = {}
        for el in nums:
            if el in hashArr:
                return True
            hashArr[el] = 1
        return False
