class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        def dp(dice, target):
            if target < 0:
                return 0
            if not dice:
                return 0 if target != 0 else 1
            if (dice, target) in memo:
                return memo[(dice, target)]
            possibleWays = 0
            for i in range(1, k+1):
                possibleWays += dp(dice-1, target-i)
            memo[(dice, target)] = possibleWays
            return possibleWays
        return dp(n,target) % (10**9 + 7)