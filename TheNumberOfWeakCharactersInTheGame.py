class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (-x[0], x[1]))
        
        answer, curMaxDef = 0,0
        for a,d in properties:
            if d < curMaxDef:
                answer += 1
            else:
                curMaxDef = d
        return answer
