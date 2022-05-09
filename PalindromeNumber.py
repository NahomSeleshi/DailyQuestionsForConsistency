class Solution:
    def isPalindrome(self, x: int) -> bool:
        xString = str(x)
        stack = []
        for char in xString:
            stack.append(char)
        stack.reverse()
        stack = "".join(stack)
        if stack == xString:
            return True
        return False
        
