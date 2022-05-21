class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        
        answer = 1
        coins.sort()
        queue = deque([each for each in coins])
        visitedCoins = set(each for each in coins)
        
        while min(queue) <= amount:
            n = len(queue)
            for i in range(n):
                temp = queue.popleft()
                if temp == amount:
                    return answer

                for coin in coins:
                    currentSum = temp + coin
                    if not currentSum in visitedCoins:
                        visitedCoins.add(currentSum)
                        queue.append(currentSum)
                
            answer += 1
            
        return -1
