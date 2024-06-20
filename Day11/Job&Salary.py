"""
ip: [(1,3),(2,5),(4,6),(6,7),(5,8),(,7,9)] ---> 1 to 3 o clock, 2 to 5 o clock soo on...
List=[5,6,5,4,11,2] 1 to 3 o clock gives 5 rupees, 2 to 5 gives 6 rupees
op: 17

"""
job=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
salary=[5,6,5,4,11,2]
i=0
m=0
j=0
s=[5,6,5,4,11,2]
for i in range(1,len(job)):
    for j in range(0,i):
        if job[i][0]>=job[j][1]:
            s[i]=max(s[]+salary[i], s[i])
print(max(s))
            

        
        
        




