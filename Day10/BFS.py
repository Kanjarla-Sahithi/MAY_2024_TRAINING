def bfstraversal():
    while queue:
        for key,values in dic.items():
            for i in dic[key]:
                if i not in queue and i not in visitedlist:
                    queue.append(i)
            x=queue.pop(0)
            visitedlist.append(x)
    print(visitedlist)
    
queue=[5]
visitedlist=[]
dic={  4:[2,6],
            2:[4,9],
            9:[2,5,12],
            5:[9,6,3],
            6:[4,5],
            1:[5,10],
            10:[1],
            3:[5],
            12:[9]
         }
key=5
print("The Visited Nodes: ")
bfstraversal()

