
# This is my first solution
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing_number = 1
        nums_set = set(nums)
        while missing_number < len(nums):
            if not missing_number in nums_set:
                break
            missing_number += 1
        num_freq = Counter(nums)
        for each in num_freq:
            if num_freq[each] == 2:
                return [each, missing_number]
        
# This is the solution that I found online

# len(nums)*(len(nums)+1)//2 gives the sum of consecutive numbers from 1 to n 
# with the formula (n*(n+1)/2)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums)-sum(set(nums)), len(nums)*(len(nums)+1)//2 - sum(set(nums))]

