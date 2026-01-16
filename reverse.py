class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node1.next=node2
node2.next=node3
node3.next=node4
prev=None
head=node1
current=head
while current is not None:
    new=current.next
    current.next=prev
    prev=current#10
    current=new#20
head=prev
current=head
while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")