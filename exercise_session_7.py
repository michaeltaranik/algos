class Node:
    def __init__(self, v):
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


def concatenate_lists(l1, l2):
    sentinel = l1
    while l1.next != None:
        l1 = l1.next
    l1.next = l2
    return sentinel


# l1 = Node(7)
# l1.next = Node(10)
# l1.next.next = Node(31)
# l2 = Node(69)
# l2.next = Node(13)
# l2.next.next = Node(777)

# l3 = concatenate_lists(l1, l2)
# print_list(l3)
# print_list(l1)
# l = reverse_list(l1)
# print_list(l)


class List:
    def __init__(self, value):
        self.value = value
        self.next = self
        self.prev = self


def list_append(l, value):
    element = List(value)
    element.prev = l.prev
    element.next = l
    element.prev.next = element
    element.next.prev = element


def print_d_list(sentinel):
    l = sentinel.next
    while l != sentinel:
        print(l.value)
        l = l.next


def reverse_double_list(l):
    sentinel = l
    while l.next != sentinel:
        l = l.next
    sentinel = l
    while l.prev != sentinel:
        print(l.value)
        l = l.prev
    print(l.value)


def concatenate_double_list(l1, l2):
    sentinel = l1
    while l1.next != sentinel:
        l1 = l1.next
    l1.next = l2
    l2.prev = l1
    l2.next.prev = l1
    return sentinel


l1 = List(None)
list_append(l1.next, 1)
list_append(l1.next.next, 2)


l2 = List(None)
list_append(l2.next, 3)
list_append(l2.next.next, 4)

print_d_list(l1)
print_d_list(l2)
l3 = concatenate_double_list(l1, l2)
print_d_list(l3)


# sentinel = List(None)
# list_append(sentinel, 1)
# list_append(sentinel.next, 2)
# print_d_list(sentinel)
# reverse_double_list(sentinel)

# sentinel = List(None)
# list_append(sentinel, 10)
# list_append(sentinel.next, 11)
# list_append(sentinel.next.next, 12)
# list_append(sentinel.prev, 9)
# print_d_list(sentinel)
