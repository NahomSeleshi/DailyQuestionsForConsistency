class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        for i in range(len(s)):
            # the index 'i' is where we start building the palindrom
            
            # this is for odd length palindroms
            answer += self.palindromeBuild(s, i, i)
            
            # this is for even length palindroms
            answer += self.palindromeBuild(s, i, i+1)
        return answer
    
    def palindromeBuild(self, string, left, right):
        count = 0
        while((left >=0 and right < len(string)) and string[left] == string[right]):
            count += 1
            left -= 1
            right += 1
        return count
