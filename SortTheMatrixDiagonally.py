class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        upwardRow = len(mat)-1
        while upwardRow >= 0:
            dRow, dCol = upwardRow, 0
            matIndex = []
            curDiagonal = []
            while dCol < len(mat[0]) and dRow < len(mat):
                matIndex.append([dRow, dCol])
                curDiagonal.append(mat[dRow][dCol])
                dCol += 1
                dRow += 1
            curDiagonal.sort()
            for i in range(len(curDiagonal)):
                mat[matIndex[i][0]][matIndex[i][1]] = curDiagonal[i]
            upwardRow -= 1
        rightwardCol = 1
        while rightwardCol < len(mat[0]):
            dRow, dCol = 0, rightwardCol
            matIndex = []
            curDiagonal = []
            while dCol < len(mat[0]) and dRow < len(mat):
                matIndex.append([dRow, dCol])
                curDiagonal.append(mat[dRow][dCol])
                dRow += 1
                dCol += 1
            curDiagonal.sort()
            for i in range(len(curDiagonal)):
                mat[matIndex[i][0]][matIndex[i][1]] = curDiagonal[i]
            rightwardCol += 1
        return mat
