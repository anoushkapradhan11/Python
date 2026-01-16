class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n=int(input("Enter the number of nodes:"))
data=int(input("Enter the value of node1:"))
node1=Node(data)
current=node1
for i in range(2,n+1):
    data=int(input(f"Enter the value of node{i}:"))
    new=Node(data)
    current.next=new
    current=new
current=node1
while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")