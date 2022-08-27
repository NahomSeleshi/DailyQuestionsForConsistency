#This approach is similar to the knapsack problem.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumOfNums = sum(nums)
        if sumOfNums % 2:
            return False
        target = sumOfNums / 2
        memo = {}
        def dfs(curSum, index):
            if curSum == target:
                return True
            if index >= len(nums) or curSum > target:
                return False
            if curSum in memo and memo[curSum][1] <= index :
                return memo[curSum][0]
            take = dfs(curSum + nums[index], index + 1)
            dontTake = dfs(curSum, index + 1)
            memo[curSum] = [take or dontTake, index]
            return take or dontTake
        return dfs(0,0)
                