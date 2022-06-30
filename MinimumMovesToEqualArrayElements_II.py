class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        mid = length // 2
        minMoves = 0
        if length % 2 == 0:
            midElement = (nums[mid-1] + nums[mid])//2
        else:
            midElement = nums[mid]
            
        for each in nums:
            minMoves += abs(each - midElement)
        
        return minMoves
