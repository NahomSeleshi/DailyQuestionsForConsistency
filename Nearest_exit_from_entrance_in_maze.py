class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        queue = deque([entrance])
        min_steps = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                if(row in [0,n-1] or col in [0, m-1]) and [row, col] != entrance:
                    return min_steps
                for r, c in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_row, new_col = row + r, col + c
                    if 0 <= new_row < n and 0 <= new_col < m and maze[new_row][new_col] == ".":
                        queue.append([new_row, new_col])
                        maze[new_row][new_col] = "+"
            min_steps += 1
        
        return -1