class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        numberOfZeros = 0
        numberOfOnes = 0
        divisionScores = []
        for i in nums:
            if i == 1:
                numberOfOnes += 1
           
        index = 0
        while index <= len(nums):
            divisionScores.append(numberOfZeros + numberOfOnes)
            if index == len(nums):
                break
            if nums[index] == 0:
                numberOfZeros += 1
            else:
                numberOfOnes -= 1
            index += 1
                
        maxValue = max(divisionScores)

        finalAnswer = []
        for index in range(len(divisionScores)):
            if divisionScores[index] == maxValue:
                finalAnswer.append(index)
                
        return finalAnswer
                
            
        
