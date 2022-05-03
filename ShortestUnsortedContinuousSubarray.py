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
    
# This is the code that I found online which is O(N) time and O(1) space.
# My implementation above is O(N) time and O(N) space.

# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
        
#         if len(nums) < 2:
#             return 0
        
#         prev = nums[0]
#         end = 0

#         for i in range(0, len(nums)):
#             if nums[i] < prev:
#                 end = i
#             else:
#                 prev = nums[i]

#         start = len(nums) - 1
#         prev = nums[start]
        
#         for i in range(len(nums)-1, -1, -1):
#             if prev < nums[i]:
#                 start = i
#             else:
#                 prev = nums[i]
                
#         if end != 0:
#             return end - start + 1
#         else: 
#             return 0
