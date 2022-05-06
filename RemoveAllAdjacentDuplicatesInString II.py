class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        letterStack = [['$',1]]
        for char in s:
            
            if char == letterStack[-1][0]:
                letterStack.append([char, letterStack[-1][1] + 1])
            
            else:
                letterStack.append([char, 1])
            
            if letterStack[-1][1] == k:
                popCounter = 0
                while popCounter < k:
                    letterStack.pop()
                    popCounter += 1
                    
        answer = ""
        index = 1
        while index < len(letterStack):
            answer += letterStack[index][0]
            index += 1
        
        return answer
            
            
