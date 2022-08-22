class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        x = (math.log(n))/(math.log(4))
        return int(x) == x
# Below is another implementation using DFS
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def helper(number):
            if number < 1:
                return False
            if number == 1:
                return True
            return helper(number/4)
        return helper(float(n))