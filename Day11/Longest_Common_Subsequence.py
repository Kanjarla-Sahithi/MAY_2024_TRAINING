s1="abcd"
s2="axbd"
m=[]
for i in range(len(s1)+1):
    l=[0]*(len(s1)+1)
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1], m[i-1][j])
print("The Longest Common Subsequence is: ", m[len(s1)][len(s2)])

a=len(s1)
b=len(s2)
s=""
while a!=0 and b!=0:
    if s1[a-1]==s2[b-1]:
        s=s+s1[a-1]
        a=a-1
        b=b-1
    else:
        if m[a][b]==m[a][b-1]:
            b=b-1
        elif m[a][b]==m[a-1][b]:
            a=a-1
print("The Longest Subsequence string is : ", s[::-1])


