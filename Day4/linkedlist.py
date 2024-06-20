"""class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(10)
b=node(20)
print(a.data, a.next)
print(b.data, b.next)"""

"""class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=node(10)
head.next=node(20)
head.next.next=node(30)
print(head.data)
print(head.next.data)
print(head.next.next.data)"""

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class sll:
    def __init__(self):
        self.head=None
        
    def addfront(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
        
    def addback(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            t=self.head
            while(t.next!=None):
                t=t.next
            new=node(data)
            t.next=new

    def display(self):
        t=self.head
        while(t!=None):
            print(t.data, end="-->")
            t=t.next
            
    def linearsearch(self,key):
        t=self.head
        while(t!=None):
            if t.data==key:
                return "found"
            else:
                t=t.next
        return "not found"

    def find_middle(self):
        t=self.head
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data

    def pairs(self):
        slow=self.head
        fast=self.head.next
        while slow.next!=None:
            while fast!=None:
                print("(",slow.data,",",fast.data,")" ,end="-->")
                fast=fast.next
            slow=slow.next
            fast=slow.next
            print()

    def bubbleSort(self):
        if self.head==None:
            return None
        else:
            t1=self.head
            c=0
            while t1:
                c+=1
                t1=t1.next                
            t1=self.head
            t2=self.head.next
            t=self.head
            temp=0
            for i in range(c):
                while t1.next and t2:
                    if t1.data>t2.data:
                        t1.data, t2.data=t2.data, t1.data
                    t1=t1.next
                    t2=t2.next
                t1=self.head
                t2=self.head.next

    def evenodd(self):
        tp=self.head
        l=self.head
        while l.next:
            l=l.next
        last=l
        temp=0
        while tp!=l:
            if tp.data%2!=0:
                if tp==self.head:
                   self.head=self.head.next
                   t=tp
                   tp=tp.next
                   temp=t.data
                   t.next=None
                   #t=tp
                   new=node(temp)
                   last.next=new
                   last=last.next
                else:
                    op=tp
                    t=self.head
                    while t.next!=tp:
                        t=t.next
                    tp=tp.next
                    t.next=op.next
                    temp=op.data
                    op.next=None
                    new=node(temp)
                    last.next=new
                    last=last.next
                    #print(t.val)
                    #print(tp.val)
                    #print(op.val)
            else:
                tp=tp.next
        if l.data%2!=0:
            if l!=self.head:
                op=tp
                t=self.head
                temp=0
                while t.next!=tp:
                    t=t.next
                tp=tp.next
                temp=op.data
                t.next=op.next
                op.next=None
                new=node(temp)
                last.next=new
                last=last.next
            else:
                t=tp
                self.head=self.head.next
                tp=tp.next
                temp=0
                temp=t.data
                t.next=None
                new=node(temp)
                last.next=new
                last=last.next

    
lis=[3,2,4,5,7,8,1]            
l1=sll()
for i in lis:
    l1.addback(i)
    
#l1.head=node(20)
#l1.addfront(52)
#l1.addfront(11)
#cl1.addback(90)
#l1.addback(54)
l1.display()
print()
#print(l1.linearsearch(1))
#print(l1.find_middle())
#l1.pairs()
#print()
#l1.bubbleSort()
l1.evenodd()
l1.display()                                                                            
        
        



