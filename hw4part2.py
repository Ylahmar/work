import re
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

s = Stack()
#stack = Stack()


s.push(54)
s.push(45)
s.push("+")

#[54,45,"+"]
#print(s.pop())
#print(s.pop())
#print(s.pop())

#[54]

while not s.is_empty():
    print(s.pop(), end=" ")


#Fullname = "Michael Chu"
#Rname = "Chu Michael"
#Y = Fullname.split(" ")
#["Michael","Chu"]
#Rname = Y[1]+ " " + Y[0]

#X="Apple sucks".split(" ")
#["Apple", "sucks"]

#print(re.split("([^0-9])", "123+456*/"))
#['123', '+', '456', '*', '', '/', '']

def eval_postfix(expr):
    import re
    token_list = re.split("([^0-9])", expr)
    print(token_list)
    stack = Stack()
    for token in token_list:
        if token == "" or token == " ":
            continue
        if token == "+":
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == "*":
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
    return stack.pop()

print(eval_postfix("2 3 * 1+ "))




['2', ' ', '3', ' ', '', '*', '', ' ', '1', ' ', '', '+', '']


















    
