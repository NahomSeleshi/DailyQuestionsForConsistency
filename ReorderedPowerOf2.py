class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digitsOfN = Counter(str(n))
        curNum = 1
        while curNum <= 10**9:
            digitsOfCurNum = Counter(str(curNum))
            if digitsOfCurNum == digitsOfN:
                return True
            curNum *= 2
        return False

# This solution is what I saw in the discussions part of leetcode

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digitsOfN = Counter(str(n))
        return any(digitsOfN == Counter(str(1<<i)) for i in range(30))