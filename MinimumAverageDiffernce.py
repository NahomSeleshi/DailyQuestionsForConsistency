class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        leftElements = 0
        rightElements = len(nums)
        leftSum = 0
        rightSum = 0
        answer = []
        for _ in range(len(nums)):
            rightSum += nums[_]
        
        totalSum = rightSum

        while leftElements < len(nums):
            currentElement = nums[leftElements]
            leftElements += 1
            rightElements -= 1
            leftSum += currentElement
            rightSum -= currentElement
            if leftSum == totalSum:
                absoluteAverage = leftSum//leftElements
                answer.append(absoluteAverage)
                continue
            absoluteAverage = (leftSum//leftElements) - (rightSum//rightElements)
            answer.append(abs(absoluteAverage))
        
        currentMin = float("inf")
        index = 0
        for i in range(len(answer)):
            if answer[i] < currentMin:
                currentMin = answer[i]
                index = i
        
        return index                  
            
