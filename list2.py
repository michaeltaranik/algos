class list_element:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None

L = list_element()
L.next = L
L.prev = L

def print_all():
    x = L.next
    while x != L:
        print(x.value)
        x = x.next

def insert_after(x, v):
    n = list_element()
    n.value = v
    n.prev = x
    n.next = x.next
    n.prev.next = n
    n.next.prev = n

def insert_before(x, v):
    n = list_element()
    n.value = v
    n.prev = x.prev
    n.next = x
    n.prev.next = n
    n.next.prev = n
