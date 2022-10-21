class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_index = {}
        for index, value in enumerate(nums):
            if value in nums_index and index-nums_index[value] <= k:
                return True
            nums_index[value] = index
        return False