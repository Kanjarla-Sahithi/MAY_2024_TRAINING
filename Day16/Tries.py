class node:
    def __init__(self):
        self.dic={}
        self.flag=0
class tries:
    def __init__(self):
        self.root=node() #Empty node is created  |{}|0|
        
    def insert(self,string):
        temp=self.root
        for i in string:
            if i not in temp.dic:
                temp.dic[i]=node()  # Here empty node is created and making a reference to other node
            temp=temp.dic[i]
        temp.flag=1
            
    def search(self,string):
        temp=self.root
        for i in string:
            if i not in temp.dic:
                return "Not Found:("
            temp=temp.dic[i]
        if temp.flag==1:
            return "Found:)"
        else:
            return "Not Found:("

    def search_prefix(self,string):
        temp=self.root
        for i in string:
            if i not in temp.dic:
                return "Not Found:("
            temp=temp.dic[i]
        return "Found:)"

    def print_all_prefix(self,string):
        def fun(temp,s):
            if temp.flag==1:
                print(s)
            for i in temp.dic:
                fun(temp.dic[i],s+i)
        temp=self.root
        s=""
        for i in string:
            if i in temp.dic:
                s=s+i
                temp=temp.dic[i]
            else:
                return
        fun(temp,s)

    def prefix_longest_string(self,string):
        def fun(t,s,res):
            if t.flag==1:
                res.append(s)
                return res
            for i in t.dic:
                res=fun(t.dic[i],s+i,res)
            return res
        t=self.root
        s=""
        for i in string:
            if i in t.dic:
                s=s+i
                t=t.dic[i]
            else:
                return
        res=fun(t,s,[])
        return res

t1=tries()
t1.insert("word")
t1.insert("apple")
t1.insert("wokeup")
t1.insert("world")
t1.insert("wore")
print("The string is",t1.search("wore"))
print("The prefix is",t1.search_prefix("w"))
t1.print_all_prefix("wo")
pr=["wo","ap"]
m=0
print()
for i in pr:
    x=t1.prefix_longest_string(i)
    for i in x:
        if m<len(i):
            m=len(i)
            r=i
print(r)
