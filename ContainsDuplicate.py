class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        numbersFrequency = Counter(nums)
        
        for eachKey in numbersFrequency:
            if numbersFrequency[eachKey] >= 2:
                return True
        return False
        
