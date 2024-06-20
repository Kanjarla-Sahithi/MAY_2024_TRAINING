#Binary Search Tree
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def create(self,data):
        if self.root==None:
            self.root=node(data)
        else:
            self.insert(self.root,data)
    def insert(self,root,data):
        if data>root.data:
            if root.right==None:
                root.right=node(data)
            else:
                self.insert(root.right,data)
        else:
            if root.left==None:
                root.left=node(data)
            else:
                self.insert(root.left,data)
                
    def inorderdisplay(self,root):
        if root:
            self.inorderdisplay(root.left)
            print(root.data,end="->")
            self.inorderdisplay(root.right)
    def preorderdisplay(self,root):
        if root:
            print(root.data,end="->")
            self.inorderdisplay(root.left)
            self.inorderdisplay(root.right)
    def postorderdisplay(self,root):
        if root:
            self.inorderdisplay(root.left)
            self.inorderdisplay(root.right)
            print(root.data,end="->")
    def sumofallnodes(self,root):
        if root==None:
            return 0
        return self.sumofallnodes(root.left) + self.sumofallnodes(root.right) + root.data
    
    def evensum(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return self.evensum(root.left) + self.evensum(root.right) + root.data
        return self.evensum(root.left) + self.evensum(root.right)

    def oddsum(self,root):
        if root==None:
            return 0
        if root.data%2!=0:
            return self.oddsum(root.left) + self.oddsum(root.right) + root.data
        return self.oddsum(root.left) + self.oddsum(root.right)

    def diffevenodd(self,root,e,o):
        if root==None:
            return 0
        if root.data%2==0:
            return self.diffevenodd(root.left,e,o) + self.diffevenodd(root.right,e,o) + root.data
        else:
            return self.diffevenodd(root.left,e,o) + self.diffevenodd(root.right,e,o) - root.data

    def height(self,root):
        if root==None:
            return -1
        return max(self.height(root.left), self.height(root.right))+1

    def balancedtree(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1

    def NoofLeafnodes(self,root):
        if root is None:
            return 0
        if root.right==None and root.left==None:
            return 1
        return (self.NoofLeafnodes(root.left)+self.NoofLeafnodes(root.right))

    def SumofLeafnodes(self,root):
        if root is None:
            return 0
        if root.right==None and root.left==None:
            return root.data
        return (self.SumofLeafnodes(root.left)+self.SumofLeafnodes(root.right))

    def Searching(self,root,key):
        if root==None:
            return 
        if root.data==key:
            return 1
        if key>root.data:
            return self.Searching(root.right,key)
        else:
            return self.Searching(root.left,key)

    def Depth(self,root,key,c):
        if root==None:
            return -1
        if root.data==key:
            return c
        if key>root.data:
            return self.Depth(root.right,key,c+1)
        else:
            return self.Depth(root.left,key,c+1)
        
    def LeftView(self,root,c,lis):
        if(root==None):
            return
        if c not in lis:
            lis.append(c)
            print(root.data, end=",")
        self.LeftView(root.left,c+1,lis)
        self.LeftView(root.right,c+1,lis)

    def RightView(self,root,c,lis):
        if(root==None):
            return
        if c not in lis:
            lis.append(c)
            print(root.data, end=",")
        self.RightView(root.right,c+1,lis)
        self.RightView(root.left,c+1,lis)

    def TopView(self,root):
        def topview(root):
            if root==None:
                return
            d={}
            q=[(root,0)]
            while(q):
                root=q[0][0]
                if root.left!=None:
                    q.append((root.left,q[0][1]-1))
                if root.right!=None:
                    q.append((root.right,q[0][1]+1))
                if q[0][1] not in d:
                    d[q[0][1]]=root.data
                q.pop(0)
            for i in sorted(d):
                print(d[i], end=" ")
        topview(root)

    def BottomView(self,root):
        def bottomview(root):
            if root==None:
                return
            d={}
            q=[(root,0)]
            while(q):
                root=q[0][0]
                if root.left!=None:
                    q.append((root.left,q[0][1]-1))
                if root.right!=None:
                    q.append((root.right,q[0][1]+1))
                d[q[0][1]]=root.data
                q.pop(0)
            for i in sorted(d):
                print(d[i], end=" ")
        bottomview(root)
    
t1=tree()
L=[10,5,15,2,7,11,8,9]
for i in L:
    t1.create(i)
t1.preorderdisplay(t1.root)
print()
t1.postorderdisplay(t1.root)
print()
t1.inorderdisplay(t1.root)
print()
print("The total Sum is ",t1.sumofallnodes(t1.root))
print("The Even Sum is ",t1.evensum(t1.root))
print(t1.inorderdisplay(t1.root.left)) #This gives only left subtree
print("The Odd Sum is ",t1.oddsum(t1.root))
print("The Difference b/w is Even and Odd", abs(t1.diffevenodd(t1.root,0,0)))
print("The Height of the Tree is ",t1.height(t1.root))
if t1.balancedtree(t1.root):
    print("Balance")
else:
    print("Not Balanced")
print("No of Leafnodes:",t1.NoofLeafnodes(t1.root))
print("Sum of LeafNodes:",t1.SumofLeafnodes(t1.root))
if t1.Searching(t1.root,15):
    print("Found")
else:
    print("Notfound")
print("Depth:",t1.Depth(t1.root,15,0))
t1.LeftView(t1.root,0,[])
print()
t1.RightView(t1.root,0,[])
print()
t1.TopView(t1.root)
print()
t1.BottomView(t1.root)


