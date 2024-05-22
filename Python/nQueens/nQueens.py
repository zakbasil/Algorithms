N = int(input("Enter the number:"))
board = [[0 for _ in range(N)] for _ in range(N)]

def isAttack(i,j):
    for k in range(0,N):
        if(board[i][k]==1 or board[k][j]==1):
            return True
    
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j or k-l==i-j):
                if (board[k][l] == 1):
                    return True
    return False

def nQueens(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if((not(isAttack(i,j))) and board[i][j]!=1):
                board[i][j] = 1
                if nQueens(n-1)==True:
                    return True
                board[i][j]=0
    return False

print(nQueens(N))
for i in board:
    print(i)

