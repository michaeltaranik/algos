class List:
    def __init__(self,v):
        self.value = v
        self.next = None

def print_list(l):
    while l != None:
        print(l.value)
        l = l.next


def reverse_list(l):
    prev = None
    while l != None:
        next = l.next
        l.next = prev
        prev = l
        l = next 
    return prev



def concatenate_lists(l1, l2):
    while l1.next != None:
        l1 = l1.next
    l1.next = l2  




l1 = List(7)
l1.next = List(10)
l1.next.next = List(11)
l1.next.next.next = List(13)
l1.next.next.next.next = List(69)
l2 = List(1)
l2.next = List(2)
l2.next.next = List(3)
l2.next.next.next = List(4)
l2.next.next.next.next = List(5)

concatenate_lists(l1, l2)
print(l1)

# print_list(l)
# l = reverse_list(l)
# print_list(l)








