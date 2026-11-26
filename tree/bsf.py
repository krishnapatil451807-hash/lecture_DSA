class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    
    def __init__(self):
        self.root = None
        self.cnt = 0       

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        temp = self.root
        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right

    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)   
        print(rt.data, end=" ")
        self.inorder(rt.right)

    def level_order(self, rt):
        if rt is None:
            print("BST is empty")
        arr=[]
        cnt=0
        level=0
        arr.append(rt)
        while(cnt<len(arr)):
            node_count=len(arr)-cnt
            print("\n level no:",level ,end=" ")
            for i in range(node_count):
                temp = arr[cnt]
                cnt+=1
                print(temp.data, end=" ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            level+=1


# b1 = BST()
b1 = BST()
for val in [100, 10, 450, 4, 65, 300, 500]:
    b1.insert(Node(val))

# b1.insert(Node(100))s
# b1.insert(Node(50))
# b1.insert(Node(30))
# b1.insert(Node(70))
# b1.insert(Node(10))

print("\nInorder : ")
b1.inorder(b1.root)

print("\nLevel order : ")
b1.level_order(b1.root)