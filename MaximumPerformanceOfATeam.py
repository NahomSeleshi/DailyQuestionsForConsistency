from heapq import heapify, heappop, heappush
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        worker = []
        for i in range(n):
            worker.append([speed[i], efficiency[i]])
        worker.sort(key = lambda x: -x[1])
        total = 0
        heap = []
        res = 0
        for i in range(k):
            total += worker[i][0]
            minE = worker[i][1]
            heapq.heappush(heap, worker[i][0])
            res = max(res, total*minE)
            
        for i in range(k, n):
            if worker[i][0] > heap[0]:
                total += (-heap[0]+worker[i][0])
                minE = worker[i][1]
                res = max(res, minE*total)
                heapq.heappop(heap)
                heapq.heappush(heap, worker[i][0])
                
        return res% (10**9 + 7)