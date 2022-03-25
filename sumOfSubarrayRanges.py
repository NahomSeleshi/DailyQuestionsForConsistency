class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sumOfSubarrays = 0
        for i in range(len(nums)-1):
            currentMax = nums[i]
            currentMin = nums[i]
            for j in range(i+1, len(nums)):
                currentMax = max(currentMax, nums[j])
                currentMin = min(currentMin, nums[j])
                sumOfSubarrays += (currentMax - currentMin)
        return sumOfSubarrays
                
        
