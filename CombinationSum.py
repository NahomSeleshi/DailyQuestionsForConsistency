class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        
        def dfs(currentList, currentSum, startIndex):
            if currentSum > target or startIndex >= len(candidates):
                return 
            
            if currentSum == target:
                self.answer.append((currentList))
                return
                
            for i in range(startIndex, len(candidates)):
                tempList = copy.deepcopy(currentList)
                tempList.append(candidates[i])
                dfs(tempList, currentSum + candidates[i], i)
        
        dfs([],0,0)
        return self.answer
        
