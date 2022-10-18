#This is the efficient solution that runs in O(nlogn) time
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search(cur_list, target):
            left, right  = 0, len(cur_list)-1
            while left <= right:
                mid = left + (right - left)//2
                if cur_list[mid] == target:
                    return mid
                elif cur_list[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return left
        LIS_list = []
        for value in nums:
            cur_index = binary_search(LIS_list, value)
            if cur_index == len(LIS_list):
                LIS_list.append(value)
            else:
                LIS_list[cur_index] = value
        return len(LIS_list)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [0 for i in range(len(nums))]
        def dp(index):
            if index == len(nums)-1:
                memo[index] = 1
                return 1
            if memo[index]:
                return memo[index]
            curLong = 0
            for i in range(index + 1, len(nums)):
                if nums[i] > nums[index]:
                    curLong = max(curLong, dp(i))
            memo[index] = curLong + 1
            return curLong + 1
        for i in range(len(nums)):
            dp(i)
        return max(memo)
