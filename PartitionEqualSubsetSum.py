# This solution is faster but I don't know why
# It's time complexity is (I think) n*2^n
# You will start a list which has 0 in it and add all the possibilities in it
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        all_possibilities = set([0])
        for number in nums:
            all_possibilities_new = list(all_possibilities)
            for each in all_possibilities_new:
                cur_number = number + each
                if cur_number == target:
                    return True
                all_possibilities.add(cur_number)
    
        return False

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
                