"""
single linked list

Kelsey Jones
"""

class LinkedList:
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            
    def __init__(self):
        self.head = None

    def __len__(self):
        """ Get length of linked list """
        length = 0

        if self.head is None:
            return length

        cur = self.head
        while cur is not None:
            length += 1
            cur = cur.next

        return length

    def append(self, value):
        """ insert the value at end of the linked list """
        new_node = self.Node(value)

        if self.head is None:
            self.head = new_node
        else:
            cur = self.head

            while cur.next is not None:
                cur = cur.next
            cur.next = new_node

    def preppend(self, value):
        """ prepend value at the end of the linked list """
        new_node = self.Node(value)

        new_node.next = self.head
        self.head = new_node

    def remove(self, value):
        """ remove value from the linked list """
        if self.head is None:
            return 0

        prev = None
        cur = self.head

        while cur is not None:
            if cur.value == value:
                if prev is None: #first node in list
                    self.head = None
                else:
                    prev.next = cur.next
                    cur.next = None

                return 0
            prev = cur
            cur = cur.next

    def search(self, value):
        """ returns True or false if value is in list """

        if self.head is None:
            return False
        else:
            cur = self.head

            while cur is not None:
                if cur.value == value:
                    return True
                cur = cur.next

            return False
            

    def __str__(self):
        """ returns string of linked list """
        str_list = ""
        str_list += "[head]-->"
        cur = self.head
        
        while cur is not None:
            str_list += ("[%s]-->"%cur.value)
            cur = cur.next

        return str_list

linked_list = LinkedList()
values = [5,2,7,7,33,1,6,0,4,3]
linked_list.preppend(999)

for num in values:
    linked_list.preppend(num)
    print(str(linked_list))
    print(len(linked_list))

for num in values:
    linked_list.remove(num)
    print(str(linked_list))
    print(len(linked_list))

print(linked_list.search(0))
print(linked_list.search(999))
linked_list.preppend(999)
print(str(linked_list))
print()
        
