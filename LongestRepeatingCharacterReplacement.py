class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFrequency = {}
        left = 0
        answer = 0
        for i in range(len(s)):
            if s[i] in charFrequency:
                charFrequency[s[i]] += 1
            else: 
                charFrequency[s[i]] = 1
            currentMax = min(max(charFrequency.values())+ k, len(s))
            
            if currentMax < (i - left) + 1:
                charFrequency[s[left]] -= 1
                left += 1
            answer = max(answer, currentMax)  
        return answer
        
