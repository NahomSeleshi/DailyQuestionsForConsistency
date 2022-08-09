class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = {}
        for each in arr:
            dp[each] = 1
        for index, a in enumerate(arr):
            for b in arr[0:index]:
                if a % b == 0:
                    key = int(a/b)
                    if key in dp:
                        dp[a] += dp[key] * dp[b]
        
        return sum(dp.values())%(10**9 + 7)