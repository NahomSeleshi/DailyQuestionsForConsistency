class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [0 for i in range(len(nums))]
        def dp(index):
            if index == len(nums)-1:
                memo[index] = 1
                return 1
            if memo[index]:
                return memo[index]
            curLong = 0
            for i in range(index + 1, len(nums)):
                if nums[i] > nums[index]:
                    curLong = max(curLong, dp(i))
            memo[index] = curLong + 1
            return curLong + 1
        for i in range(len(nums)):
            dp(i)
        return max(memo)