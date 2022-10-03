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