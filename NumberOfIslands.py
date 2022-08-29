class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            grid[row][col] = "0"
            if row > 0 and grid[row-1][col] == "1":
                dfs(row-1, col)
            if row < len(grid)-1 and grid[row+1][col] == "1":
                dfs(row+1, col)
            if col > 0 and grid[row][col-1] == "1":
                dfs(row, col-1)
            if col < len(grid[0])-1 and grid[row][col+1] == "1":
                dfs(row, col+1)
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    answer += 1
        return answer
                