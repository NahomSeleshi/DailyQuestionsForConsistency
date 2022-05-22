from fractions import Fraction
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        slopes = []
        stockPrices.sort()
        if len(stockPrices) == 1: return 0
        
        for i in range(len(stockPrices)-1):
            firstPoint, secondPoint = stockPrices[i], stockPrices[i+1]
            currentSlope = Fraction(secondPoint[1] - firstPoint[1], secondPoint[0] - firstPoint[0])
            slopes.append(currentSlope)

        lines = 1
        for i in range(len(slopes)-1):
            if slopes[i] != slopes[i+1]:
                lines += 1
                
        return lines
