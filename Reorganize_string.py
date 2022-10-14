from heapq import heapify, heappop, heappush
class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = []
        heapify(maxHeap)
        char_freq = collections.Counter(s)
        for key, value in char_freq.items():
            heappush(maxHeap, [-value, key])
        answer = []
        prev_char, prev_count = '', 0
        while maxHeap:
            cur_char = heappop(maxHeap)
            answer.append(cur_char[1])
            
            if prev_count < 0:
                heappush(maxHeap, [prev_count, prev_char])
                
            prev_count = cur_char[0] + 1
            prev_char = cur_char[1]
            
        ans = "".join(answer)
        return "" if len(ans) != len(s) else ans