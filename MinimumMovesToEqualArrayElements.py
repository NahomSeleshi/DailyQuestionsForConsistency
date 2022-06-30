class Solution:
    def minMoves(self, nums: List[int]) -> int:
        '''
        -Instead of trying to increment n-1 elements by 1, we can decrease 1 from the max element
        -So, this problem becomes counting how many steps needed to equalize every element with the
         min element in the list. When we equalize the max element with the min one, other number in 
         the list becomes max and we will also decrement it until all the elements in the list are 
         equal to min.
        '''
        minElement = min(nums)
        minMoves = 0
        
        for each in nums:
            minMoves += each-minElement
        
        return minMoves
