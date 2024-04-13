#Linked list

class List_element:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None

sentinel = List_element()
sentinel.next = sentinel
sentinel.prev = sentinel


def insert_after(element, value):
    n = List_element()
    n.value = value
    n.next = element.next
    n.prev = element
    n.prev.next = n
    n.next.prev = n

 
def print_all():
    x = sentinel.next
    while x.next != sentinel:
        print(x.value)
        x = x.next

for i in range(10):
    insert_after(sentinel, i)


print_all()










