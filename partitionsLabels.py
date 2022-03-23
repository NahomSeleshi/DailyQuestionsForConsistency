class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        answer = []
        left = 0
        right = 0
        temp = set()
        temp1 = set()
        while left < len(s):
            if left == right:
                temp.add(s[left])
            right += 1
            while right < len(s):
                if s[right] in temp:
                    left = right
                    temp.update(temp1)
                    temp1.clear()
                    right +=1
                else:
                    temp1.add(s[right])
                    right +=1
            temp.clear()
            temp1.clear()
            left +=1
            right = left
            totalSum = sum(answer)
            answer.append(left-totalSum) if answer else answer.append(left)
        return answer
                
                
        
