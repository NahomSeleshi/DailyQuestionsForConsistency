class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        curTimes = []
        minimumTime = 0
        for i in range(len(colors)-1):
            if colors[i] == colors[i+1]:
                curTimes.append(neededTime[i])
            else:
                if len(curTimes) > 0:
                    curTimes.append(neededTime[i])
                    minimumTime += sum(curTimes) -max(curTimes)
                    curTimes.clear()
        if len(colors) > 1 and (colors[-1] == colors[-2]):
            curTimes.append(neededTime[-1])
            minimumTime += sum(curTimes) -max(curTimes)
            
        return minimumTime

# This is a solution that I found on Leetcode solution section and 
# it is somehow optimized than my solution

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i, j = 0, 0
        minimumTime = 0
        while i < len(colors) and j < len(colors):
            curTotal, curMax = 0, 0
            while j < len(colors) and colors[i] == colors[j]:
                curTotal += neededTime[j]
                curMax = max(curMax, neededTime[j])
                j += 1
            minimumTime += curTotal - curMax
            i = j
            
        return minimumTime
