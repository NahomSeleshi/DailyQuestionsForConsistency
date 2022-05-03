class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        tempArray = nums.copy()
        tempArray.sort()
        left, right = 0, len(nums)-1
        
        for i in range(len(nums)):
            left = i
            if nums[i] != tempArray[i]:
                break
        
        for j in range(len(nums)-1, -1, -1):
            right = j
            if nums[j] != tempArray[j]:
                break
        shortestLength = abs(right - left) + 1
        
        if left == len(nums)-1 and right == 0:
            return 0
        return shortestLength
