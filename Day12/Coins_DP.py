coins=[2,3,4]
val=11
dp=[]
for i in range(len(coins)):
    l=[-1]*(val+1)
    dp.append(l)

for i in range(len(coins)):
    for j in range(val+1):
        if coins[i]==j:
            dp[i][j]=1
            continue
        if coins[i]>j:
            dp[i][j]=dp[i-1][j]
            continue
        if coins[i]<j:
            x=j-coins[i]
            if dp[i][x]==-1:
                if dp[i-1][j]>0:
                    dp[i][j]=dp[i-1][j]
                    continue
                dp[i][j]=-1
                continue
            else:
                dp[i][j]=dp[i][x]+1
            
for i in dp:
    print(i)