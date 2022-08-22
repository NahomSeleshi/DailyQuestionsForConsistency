class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        x = (math.log(n))/(math.log(4))
        return int(x) == x