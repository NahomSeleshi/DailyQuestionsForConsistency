class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        answer = set()
        setOfDNASequences = set()
        left = 0
        right = 10
        while right <= len(s):
            currentString = s[left:right]
            if currentString in setOfDNASequences:
                answer.add(currentString)
            else:
                setOfDNASequences.add(currentString)
            left += 1
            right += 1
        return list(answer)
