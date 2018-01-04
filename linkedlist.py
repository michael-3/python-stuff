class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

class List(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def find(self, value):
        current = self.head
        while (current != None):
            if (current.value == value):
                return current
            current = current.next
        return None

    def append(self, value):
        node = Node(value)
        if (self.size == 0):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def prepend(self, value):
        node = Node(value)
        if (self.size == 0):
            self.head = none
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def show(self):
        current = self.head
        display = ""
        while(current != None):
            display += str(current.value)
            display += "->"
            current = current.next
        display += "None"
        print display

    # deletes all nodes with value
    def delete(self, value):
        current = self.head
        previous = None
        while (current != None):
            if (current.value == value):
                self.size -= 1
                # case where element at the head
                if (previous == None):
                    self.head = current.next
                # case where lement is after the head
                else:
                    previous.next = current.next
            else:
                previous = current
            current = current.next

class CircularList(object):
