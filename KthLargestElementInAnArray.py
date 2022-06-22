class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pointer = len(nums)-k
        nums.sort()
        return nums[pointer]
