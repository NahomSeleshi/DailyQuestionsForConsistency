class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(len(nums)):
            if not i in nums:
                return i
        return len(nums)
        
