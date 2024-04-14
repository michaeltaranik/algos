class List:
    def __init__(self, v):
        self.value = v
        self.next = None


def print_all(element):
    while element != None:
        print(element.value)
        element = element.next
