"""
Problem 2.3

implement an algorithm to delete a node in the middle of a
singly linked list given acces only to that node.

"""

from linked_list import LinkedList

def delete_mid_node(middle_node):
    if middle_node is None:
        return 0

    if middle_node.next is not None:
        middle_node.value = middle_node.next.value
        middle_node.next = middle_node.next.next
        middle_node.next.next = None

    return middle_node


linked_list = LinkedList()
letters = ['a', 'b', 'c', 'd', 'e']

for let in letters:
    linked_list.append(let)

print(str(linked_list))

mid_node = linked_list.get_node('c')
print(str(mid_node))

print(str(delete_mid_node(mid_node)))
print(str(linked_list))

