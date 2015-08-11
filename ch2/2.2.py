"""
Problem 2.2. Implement an algorithm to find the kth to last
element of a singly linked list.
"""

from linked_list import LinkedList

def find_k_elem(linked_list, k_num):
    """ Returns None is not found or the Node element """
    k_elem = None
    cur = linked_list
    count = 0

    while cur is not None:
        count += 1

        if count == k_num:
            k_elem = linked_list
        elif count > k_num:
            k_elem = k_elem.next

        cur = cur.next

    return k_elem

def main():       
    linked_list = LinkedList()
    values = [5,2,7,7,33,1,6,0,4,3]

    for num in values:
        linked_list.append(num)

    print(str(linked_list))

    #find 1st to last
    print(find_k_elem(linked_list.head, 1).value)
    #find 2nd to last
    print(find_k_elem(linked_list.head, 2).value)
    #find 6th to last
    print(find_k_elem(linked_list.head, 6).value)
    #find 33 to last elem
    print(find_k_elem(linked_list.head, 33))   

if __name__ == "__main__":
    main()
