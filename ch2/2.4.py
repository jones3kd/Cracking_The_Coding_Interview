"""
write code to partition 
a linked list aroung a value x, such that all nodes less than x 
come before all nodes greater than or equal to x
"""
from linked_list import LinkedList

def partition(linked_list, value):
    #value is not necessarily a node in the list
    #go through linked list
    #make head for first half
    #mid_head
    #once go through whole linked list link end of head to mid_head

    head = None
    last_list_elem = None
    mid_head = None
    last_mid_elem = None
    cur = linked_list

    while cur is not None:
        if cur.value < value:
            if head is None:
                head = cur
                last_list_elem = cur
            else:
                last_list_elem.next = cur
                last_list_elem = cur
        else:
            if mid_head is None:
                mid_head = cur
                last_mid_elem = cur
            else:
                last_mid_elem.next = cur
                last_mid_elem = cur
                
        cur = cur.next

    #link two halfs of the linked list
    last_list_elem.next = mid_head       

linked_list = LinkedList()
letters = [5, 76, 0, 2323, 5454, 4, 2, 6, 3, 9, 55]

for let in letters:
    linked_list.append(let)

print(str(linked_list))
partition(linked_list.head, 55)
print(str(linked_list))







    
