class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints)-k
        currentMinSum = sum(cardPoints[:size])
        currentSum = currentMinSum
        for i in range(1, k+1):
            currentSum = currentSum + cardPoints[i+size-1] - cardPoints[i-1]
            currentMinSum = min(currentMinSum, currentSum)
            
        return sum(cardPoints) - currentMinSum
