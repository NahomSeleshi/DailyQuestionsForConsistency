class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1])
        answer = 0
        for i in range(len(boxTypes)-1, -1, -1):
            currentBoxNum = boxTypes[i][0]
            if currentBoxNum > truckSize:
                answer += (truckSize * boxTypes[i][1])
                break
            else:
                answer += (currentBoxNum * boxTypes[i][1])
                truckSize -= currentBoxNum
        return answer
