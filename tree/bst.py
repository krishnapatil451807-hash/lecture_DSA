class node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value
class BST:
    def __init__(self):
        self.root=None
        self.cnt=0
        self.ncnt=0
    def insert(self,new_node):
        if self.root is None :
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
    def inorder(self,rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            if rt.left is None and rt.right is None:
               self.cnt+=1
            print(rt.data,end=" ")
            self.inorder(rt.right)
    def preorder(self,rt):
        if rt is None:
            return
        else:
            print(rt.data,end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)
    def postorder(self,rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")
    def findmin(self,rt):
        temp=rt
        while temp.left:
            temp=temp.left
        print("\n min",temp.data)
    def findmax(self,rt):
        temp=rt
        while temp.right:
            temp=temp.right
        print("\n max",temp.data)
    def del_node(self, rt, val):
        if rt is None:
            return rt
        if val < rt.data:
            rt.left = self.del_node(rt.left, val)
        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)
        else:
            
            if rt.left is None: #node with right child only
                return rt.right
            if rt.right is None: #node with left child only
                return rt.left

            # Node with 2 children (succ = inorder successor)
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right, succ.data)
    def count_nleaf(self,rt):
        if rt is None:
            return
        else:
            self.count_nleaf(rt.left)
            if rt.left is not None or rt.right is not None:
                self.ncnt+=1
            self.count_nleaf(rt.right)
    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key<temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return False
b1=BST()
b1.insert(node(100))
b1.insert(node(10))
b1.insert(node(450))
b1.insert(node(50))
b1.insert(node(65))
b1.insert(node(300))

# print("inorder")
b1.inorder(b1.root)

# print("\npreorder")
# b1.preorder(b1.root)

# print("\npostorder")
# b1.postorder(b1.root)
# b1.findmin(b1.root)
# b1.findmax(b1.root)
print("\n total no leaf node ",b1.cnt)
if b1.search(50):
    print("\n found the node")
else:
    print("\n not found")
b1.count_nleaf(b1.root)
print("\n non leaf node count",b1.ncnt)