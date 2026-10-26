class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class queue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def dequeue(self):
        if self.front:
            temp=self.front
            self.front=self.front.next
            if self.front==None:
                self.rear=None
                print("now queue is empty")
            temp=None
        else:
            print("Queue is empty")
    def print(self):
        temp=self.front
        print("queue data")
        while temp:
            print(temp.data,"->")
            temp=temp.next
que=queue()
que.enqueue(node(15))
que.enqueue(node(67))
que.enqueue(node(55))
que.enqueue(node(100))
que.enqueue(node(88))
que.print()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.print()