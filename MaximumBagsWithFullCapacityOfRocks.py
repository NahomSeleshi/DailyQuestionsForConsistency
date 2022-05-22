class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        difference = []
        for i in range(len(rocks)):
            difference.append(capacity[i] - rocks[i])
            
        difference.sort()
        index, answer = 0, 0
        while additionalRocks > 0 and index < len(difference):
            if additionalRocks >= difference[index]:
                answer += 1
            if difference[index] == 0:
                index += 1
                continue
            additionalRocks -= difference[index]
            index += 1
            
        return answer
