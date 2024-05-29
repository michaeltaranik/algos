from unittest.mock import sentinel


class ListNode:
    def __init__(self, v) -> None:
        self.data = v
        self.next = None


# List 1: 1 -> 2 -> 4
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3


# List 2: 1 -> 3 -> 5
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(5)
node4.next = node5
node5.next = node6
node6.next = ListNode(10)
node6.next.next = ListNode(20)


def print_all(node):
    while node != None:
        print(node.data)
        node = node.next


def merge_two_sorted_lists(l1, l2):
    sentinel = ListNode(0)
    current = sentinel

    while l1 != None and l2 != None:

        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
            current = current.next

        elif l1.data >= l2.data:
            current.next = l2
            l2 = l2.next
            current = current.next

    if l1 != None:
        current.next = l1
    elif l2 != None:
        current.next = l2

    return sentinel.next


# print_all(node1)
# print_all(node4)
print_all(merge_two_sorted_lists(node1, node4))
