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
new=Node(25)
head=node1
while head is not None and head.data!=20:
    head=head.next
new.next=head.next
head.next=new
head= node1
while head is not None:
    print(head.data,end="->")
    head=head.next
print("None")