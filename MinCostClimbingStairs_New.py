class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = ['_' for i in range(len(cost))]
        def DFS(index):
            if index >= len(cost):
                return 0
            if index == len(cost)-1:
                dp[index] = cost[-1]
                return cost[-1]
            if dp[index] != '_':
                return dp[index]
            oneStep = cost[index] + DFS(index+1)
            twoStep = cost[index] + DFS(index+2)
            currentMinCost = min(oneStep, twoStep)
            dp[index] = currentMinCost
            return currentMinCost
        DFS(0)
        return min(dp[0], dp[1])
