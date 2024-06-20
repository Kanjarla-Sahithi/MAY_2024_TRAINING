#NQueens
def backtrack(r,col,posdig,negdig,res,board,flag,x,m):
    m=max(len(x),m)
    if r>n-1:
        l=["".join(i) for i in board]
        res.append(l)
        flag+=1
        return res,flag,m
    if r in row:
        res,flag,m=backtrack(r+1,col,posdig,negdig,res,board,flag,x,m)
    for c in range(n):
        if c in col or (r+c) in posdig or (r-c) in negdig:
            continue
        board[r][c]="  Q  "
        x.append(1)
        col.append(c)
        posdig.append(r+c)
        negdig.append(r-c)

        res,flag,m=backtrack(r+1,col,posdig,negdig,res,board,flag,x,m)
        x.pop()
        board[r][c]="  _  "
                
        col.remove(c)
        posdig.remove(r+c)
        negdig.remove(r-c)
    return res,flag,m
x=[]
col=[]
row=[]
posdig=[]
negdig=[]
n=6
a=int(input("enter row coordinates of rook"))
b=int(input("enter col coordinates of rook"))
board=[["  _  "]*n for i in range(n)]
board[a][b]="  R  "
col=[b]
row=[a]
res,flag,x=backtrack(0,col,posdig,negdig,[],board,0,x,0)
print("maximum number of queens :", x)

