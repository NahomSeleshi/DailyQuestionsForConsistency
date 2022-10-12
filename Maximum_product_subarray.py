class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod, min_prod, answer = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], max_prod * nums[i], min_prod * nums[i])
            cur_min = min(nums[i], max_prod*nums[i], min_prod * nums[i])
            max_prod, min_prod = cur_max, cur_min
            answer = max(answer, max_prod)
        return answer