class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInteger = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        answer = 0
        for i in range(len(s)-1):
            if romanToInteger[s[i]] >= romanToInteger[s[i+1]]:
                answer += romanToInteger[s[i]]
            else:
                answer-= romanToInteger[s[i]]
        answer += romanToInteger[s[-1]]
        return answer
        
