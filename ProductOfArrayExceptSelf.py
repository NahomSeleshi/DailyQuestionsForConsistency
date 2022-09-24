class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [1]*n , [1]*n
        product_array = []
        
        #populate the left array
        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]
        
        #populate right array
        newNums = nums[::-1]
        for j in range(1,n):
            right[j] = right[j-1] * newNums[j-1]
        right.reverse()
        
        for i in range(n):
            product_array.append(left[i]*right[i])
        return product_array