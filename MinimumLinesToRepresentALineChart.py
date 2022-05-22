#This is the code that I edited my first one with some new implementations
# like using pairwise in the for loop

from fractions import Fraction
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        slopes = []
        stockPrices.sort()
        if len(stockPrices) == 1: return 0
        
        lines = 1
        prevSlope = Fraction(stockPrices[1][1]-stockPrices[0][1], stockPrices[1][0]-stockPrices[0][0])
        for first, second in pairwise(stockPrices):
            newGradient = Fraction(second[1]-first[1], second[0]-first[0])
            if newGradient != prevSlope:
                prevSlope = newGradient
                lines +=1
           
        return lines

#This is my first code
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
