K = int(input())
chessboard = [[0 for _ in range(K)] for _ in range(K)] 

def isAttacking(i,j):
    for l in range(K):
        if chessboard[i][l] == 1 or chessboard[l][j] == 1:
            return(True)
    for l in range(K):
        for m in range(K):
            if l+m == i+j and chessboard[l][m] == 1:
                return(True)
            if l-m == i-j and chessboard[l][m] == 1:
                return(True)
    return(False)

def nQueens(n):
    if n == 0:
        return(True)
    for i in range(K):
        for j in range(K):
            if not isAttacking(i,j) and chessboard[i][j] == 0:
                chessboard[i][j] = 1
                if nQueens(n-1):
                    return(True)
                chessboard[i][j] = 0
    return(False)

print(nQueens(K))