class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            oddPalindrome = self.palindromeBuild(s, i, i)
            evenPalindrome = self.palindromeBuild(s, i, i+1)
            if len(oddPalindrome) > len(evenPalindrome):
                if len(answer) < len(oddPalindrome):
                    answer = oddPalindrome
            else:
                if len(answer) < len(evenPalindrome):
                    answer = evenPalindrome
        return answer
            
    def palindromeBuild(self, string, left, right):
        currentPalindrome = deque([])
        while((left>=0 and right < len(string)) and string[left] == string[right]):
            if left == right:
                currentPalindrome.append(string[left])
            else:
                currentPalindrome.appendleft(string[left])
                currentPalindrome.append(string[right])
            left -= 1
            right +=1
        return "".join(currentPalindrome)
