class List:
    def __init__(self):
        pass

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for i in range(n)]

        nxt = 1
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        d = 0
        r = 0
        c = 0
        while nxt <= n*n:
            matrix[r][c] = nxt

            if r + dx[d] == n or c + dy[d] == n or matrix[r+dx[d]][c+dy[d]] != 0 :
                d = (d + 1) % 4

            r += dx[d]
            c += dy[d]
            nxt += 1

        return matrix
