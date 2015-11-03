""" create a set of stacks that have a capacity"""

class SetOfStacks:

    class Stack:
        """ each stack has it's own prev stack variable """
        def __init__(self, prev_stack = None):
            self.length = 0
            self.prev_stack = prev_stack
            self.list = []

        def get_length(self):
            return self.length

        def pop(self):
            popped_item = None
            popped_item = self.list[-1]
            del self.list[-1]
            self.length -= 1

            return popped_item

        def push(self, item):
            self.list.append(item)
            self.length += 1
            print(self.list)

        def __str__(self):
            str_list = ""
            for elem in self.list:
                str_list += str(elem) + "<-"

            return str_list

    def __init__(self, capacity = 5):
        self.cur_stack = self.Stack()#create first stack
        self.capacity = capacity

    def _create_new_stack(self):
        """create new stack and set curStack to this stack"""
        new_stack = self.Stack()#always keep a stack
        new_stack.prev_stack = self.cur_stack
        self.cur_stack = new_stack

    def pop(self):
        """ pop item from stack. if stack length is 0 delete stack """
        item = self.cur_stack.pop()

        if (self.cur_stack.prev_stack is not None and
            self.cur_stack.get_length() < 1):
            #delete the stack
            self.cur_stack = self.cur_stack.prev_stack

        return item

    def push(self, item):
        """
        check if curStack reached capacity, if so creates a new stack
        """
        if self.cur_stack.get_length() >= self.capacity:
            self._create_new_stack()

        self.cur_stack.push(item)

    def __str__(self):
        str_stack = ""
        cur = self.cur_stack
        while cur is not None:
            str_stack = " | " + str(cur) + str_stack
            cur = cur.prev_stack

        return str_stack

set_of_stacks = SetOfStacks()
nums = [5,2,6,7,3,3,2,6,1,2,3,4,5]

for num in nums:
    set_of_stacks.push(num)

print(str(set_of_stacks))

print(set_of_stacks.pop())
print(set_of_stacks.pop())
print(set_of_stacks.pop())
print(str(set_of_stacks))
print(set_of_stacks.pop())
print(str(set_of_stacks))
print(set_of_stacks.pop())
