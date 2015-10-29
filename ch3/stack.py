#create a stack

class Stack:

    def __init__(self):
        self.length = 0
        self.values = []
        pass

    def push(self, item):
        self.values.append(item)
        self.length += 1

    def pop(self):
        val = self.values[-1]
        del self.values[-1]

        return val

    def peek(self):
        return self.values[-1]

    def __len__(self):
        return self.length

    def __str__(self):
        "Return printed version of stack"
        str_val = ""
        for val in self.values:
            str_val += str(val) + "->"

        return str_val

vals = [4,3,6,1,3,5,65,65,3,43,43,2,23,88,433]
stack = Stack()
for num in vals:
    stack.push(num)

print(str(stack))
stack.pop()
print(str(stack))
stack.pop()
print(stack.peek())

print(str(stack))
