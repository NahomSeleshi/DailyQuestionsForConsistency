class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = Counter(nums)
        sequence = defaultdict(int)
        
        for each in nums:
            if not left[each]:
                continue
            if sequence[each-1]:
                sequence[each-1] -= 1
                sequence[each] += 1
                left[each] -= 1
            else:
                if not left[each + 1] or not left[each + 2]:
                    return False
                left[each] -= 1
                left[each + 1] -= 1
                left[each + 2] -= 1
                sequence[each+2] += 1
        return True

                
                