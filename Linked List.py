class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Utility function to find the last node in a list segment
def get_tail(node):
    while node and node.next:
        node = node.next
    return node

# Partition function to rearrange nodes around a pivot
def partition(head, end):
    pivot = head  # Use the head as the pivot
    prev, curr = head, head.next  # Initialize pointers for traversal

    while curr != end:
        if curr.val < pivot.val:
            prev = prev.next
            prev.val, curr.val = curr.val, prev.val  # Swap values
        curr = curr.next

    # Place the pivot in its correct position
    head.val, prev.val = prev.val, head.val
    return prev  # Return pivot position

# Recursive quicksort function for linked list
def quicksort_recur(start, end):
    if start != end:
        pivot = partition(start, end)
        quicksort_recur(start, pivot)       # Sort left of pivot
        quicksort_recur(pivot.next, end)    # Sort right of pivot

# Main quicksort function
def quickSort(head):
    quicksort_recur(head, None)
    return head

# Helper function to print the list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage
if __name__ == "__main__":
    # Creating a linked list: 1 -> 6 -> 2
    ll = ListNode(1, ListNode(6, ListNode(2)))
    print("Original List:")
    printList(ll)

    # Sort the list
    sorted_list = quickSort(ll)
    print("Sorted List:")
    printList(sorted_list)
