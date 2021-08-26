class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
    def print_backward(self):
        print("[", end=" ")
        if self.head is not None:
            self.head.print_backward()
    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=" ")

Y = LinkedList()
Y.add_first("test")
Y.add_first("test2")
print(Y.head)
print(Y.length)



node1 = Node(1)
#node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
def print_list(x):
    print("[", end=" ")
    
    while x is not None:
        print(x, end="")
        if x.next:
            print(end=',')
        x = x.next   
    print(']')
        
    

print_list(node1)

def print_backward(list):
    if list is None: return
    head = list
    tail = list.next
    print_backward(tail)
    print(head, end="  ")


def remove_second(list):
    if list is None: return
    first = list
    second = list.next
    # Make the first node refer to the third
    first.next = second.next
    # Separate the second node from the rest of the list
    second.next = None
    return second

def print_backward_nicely(list):
    print("[", end=" ")
    print_backward(list)
    print("]")

print_backward_nicely(node1)









