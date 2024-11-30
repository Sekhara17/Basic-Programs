class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
head=Node(0)
dummy=head
#create a linked list using for loop
for i in range(1,11):
    dummy.next=Node(i) 
    dummy=dummy.next 






#creating linked list using arr
arr=[10,20,30,40,50,60,70]
head1=Node(1)
def arrayToll(head1,arr):
    temp1=head1
    for i in range(len(arr)):
        temp1.next=Node(arr[i])
        temp1=temp1.next
  



#printing linked list function
def printll(head):
    while head:
        print(head.data ,end="->")
        head=head.next
    print("NULL") 


#reversing a linked list
def revLL(head1):
    prev=None
    curr=head1
    while curr:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
    return prev


#insert a node at the end of linkedlist
#def linkedl(head1):


arrayToll(head1,arr)
h=revLL(head1) 
printll(h)
      
