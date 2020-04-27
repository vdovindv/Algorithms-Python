def uniquePaths(self, m: int, n: int) -> int:
        res = [[0]*m]*n
        
        for i in range(n):
            res[i][0] = 1
            
        for i in range(m):
            res[0][i] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]
