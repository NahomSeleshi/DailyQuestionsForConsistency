class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adjacencyMat = [[]for i in range(n)]
        for x,y in edges:
            adjacencyMat[x].append(y)
            adjacencyMat[y].append(x)
        queue = deque()
        queue.append(0)
        visitedNodes = set()
        restricted = set(restricted)
        while queue:
            currentNode = queue.popleft()
            visitedNodes.add(currentNode)
            for each in adjacencyMat[currentNode]:
                if not each in restricted and not each in visitedNodes:
                    queue.append(each)
                    
        return len(visitedNodes)