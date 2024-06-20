def dijkstras(x):
    while queue:
        for i in dic[x]:
            if i[0] not in visited:
                queue.append(i[0])
                c=cost[x]+i[1]
                if cost[i[0]]>c:
                    cost[i[0]]=c
        x=queue.pop(0)
        visited.append(x)
        m=99999
        for i in queue:
            m=min(cost[i],m)
            x=i
    print(cost)                

visited=[]
queue=[5]
dic={
          5:[(8,2),(3,2),(2,2)],
          2:[(5,2),(3,1)],
          8:[(5,2),(3,3),(6,4)],
          3:[(5,2),(2,1),(8,3),(7,3)],
          7:[(3,3),(9,1)],
          6:[(8,4),(9,2)],
          9:[(6,2),(7,1),(4,2)],
          4:[(9,2)]
         }
cost={
           5:999999,
           2:999999,
           8:999999,
           3:999999,
           7:999999,
           6:999999,
           9:999999,
           4:999999,
           }
cost[5]=0
dijkstras(5)
