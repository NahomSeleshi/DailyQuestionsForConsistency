class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        operations = 0
        
        while left < right:
            currentSum = nums[left] + nums[right]
            if currentSum == k:
                operations += 1
                left += 1
                right -= 1
            elif currentSum < k:
                left += 1
            else:
                right -= 1
        return operations
        
