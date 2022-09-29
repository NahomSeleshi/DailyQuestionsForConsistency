class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pts_dist = []
        for each in arr:
            curDist = abs(each-x)
            pts_dist.append([curDist, each])
        pts_dist.sort(key = lambda x: (x[0], x[1]))
        
        answer = []
        index = 0
        while index < k:
            answer.append(pts_dist[index][1])
            index += 1
        
        return sorted(answer)