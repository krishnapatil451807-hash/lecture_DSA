class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp=self.top
            print("poed element",temp.data)
            self.top=self.top.next
            temp=None
    def reverse(self):
        temp=self.top
        while temp:
            sta1.push(node(temp.data))
            temp=temp.next
    def print(self):
        temp=self.top
        print("stack data")
        while temp:
            print(temp.data)
            temp=temp.next
sta=stack()
sta1=stack()
sta.push(node(10))
sta.push(node(100))
sta.push(node(45))
sta.push(node(87))
sta.push(node(50))
sta.print()
# sta.pop()
sta.print()
sta.reverse()
sta1.print()