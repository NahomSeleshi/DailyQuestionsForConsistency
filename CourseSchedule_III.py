from heapq import heapify, heappop, heappush
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])
        maxHeap = []
        heapify(maxHeap)
        currentStart = 0
        
        for duration, end in courses:
            currentStart += duration
            heappush(maxHeap, -duration)
            
            if currentStart > end:
                currentDuration = heappop(maxHeap)
                currentStart += currentDuration
                
        return len(maxHeap)
