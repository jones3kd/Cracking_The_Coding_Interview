"""
Binary Search Tree

remove not working yet


      7
    5  9
  2   6   12
 1 3
 """

class BinarySearchTree:
    """ A binary search tree """

    class Node:
        def __init__(self, value=None):
            self.value = value
            self.left = None
            self.right = None

        def insert(self, new_node):
            """ recursively inserts the value into the tree """
            if new_node.value < self.value:
                #go left
                if self.left is not None:
                    self.left.insert(new_node)
                else:
                    self.left = new_node
            else:#go right
                if self.right is not None:
                    self.right.insert(new_node)
                else:
                    self.right = new_node

        def find_successor(self, parent):
            """ searches recurseivly down until it finds a node without
             a  child """

            if self.left is None and self.right is None:
                print("no child for this node: "+str(self.value))
                #delete itself from parent
                if self.value < parent.value:
                    parent.left = None
                else:
                    parent.right = None
                return self
            else:
                if self.left is not None:
                    return self.left.find_successor(self)
                elif self.right is not None:
                    return self.right.find_successor(self)

        def remove(self, parent, value):
            """ removes value from tree
            returns successor if vlaue removed was the root"""
            on_left = False #child of parent
            if self.value == value:
                #no children
                if parent is not None:
                    print("found, parent is: " + str(parent.value))
                    if value < parent.value: #was left child
                        parent.left = None
                        on_left = True
                    else:
                        parent.right = None

                    if self.left is None and self.right is None:
                        #no children
                        pass
                    elif self.right is not None and self.left is None:
                        #one child just replace pointer to parent
                        if on_left:
                            parent.left = self.right
                        else:
                            parent.right = self.right
                    elif self.left is not None and self.right is None:
                        #one child just replace pointer to parent
                        if on_left:
                            parent.left = self.left
                        else:
                            parent.right = self.left
                    else:#2 children
                        #find successor
                        successor = self.right.find_successor(self)

                        if on_left:
                            parent.left = successor
                        else:
                            parent.right = successor
                else:#removing root of tree so must update self.root in
                    #binary tree
                    if self.left is None and self.right is None:
                        #no children
                        pass
                    elif self.right is not None and self.left is None:
                        #one child just replace pointer to parent
                        return self.right

                    elif self.left is not None and self.right is None:
                        #one child just replace pointer to parent
                        return self.left

                    else:#2 children
                        #find successor
                        successor = self.right.find_successor(self)

                        return successor


            else:#didn't find value continue search
                if self.left is not None:
                    self.left.remove(self, value)

                if self.right is not None:
                    self.right.remove(self, value)


        def print_tree(self):
            """ print and search in order """

            #go left
            if self.left is not None:
                self.left.print_tree()

            print(str(self.value) + " "),

            if self.right is not None:
                self.right.print_tree()
            #go right

    def __init__(self):
        self.root = None
        self.height = 0

    def insert(self, value):
        """ inserts a new value into the tree """
        new_node = self.Node(value)

        #recursively with the node methods
        if self.root is not None:
            self.root.insert(new_node)
        else:
            self.root = new_node

    def remove(self, value):
        """ removes the value from the binary tree if found """
        if self.root is not None:
            succ = self.root.remove(None, value)

        if succ is not None:
            self.root = succ

    def print_tree(self):
        """ prints tree in sorted order """
        if self.root is not None:
            self.root.print_tree()
        print("\n")


tree = BinarySearchTree()

print("test")

nums = [20,7,44,2,2,7,900,11,46,33]

for num in nums:
    tree.insert(num)

tree.print_tree()

for num in nums:
    tree.remove(num)
    tree.print_tree()

print("final: ")
tree.print_tree()
