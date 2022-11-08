class Solution:
    def makeGood(self, s: str) -> str:
        index = 0
        while index < len(s) -1:
            if abs(ord(s[index]) - ord(s[index+1])) == 32:
                s = s[:index] + s[index+2:]
                index = 0
            else:
                index += 1
        return s