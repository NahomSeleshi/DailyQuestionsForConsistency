class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums1 = []
        for each in nums:
            nums1.append(int(each))
        nums1.sort()
        return str(nums1[len(nums1) - k])
