class LinkedList:

    # create head - starting point for iterations
    def __init__(self):
        self.head = None

    # add new node to end of the list
    def insert(self, data):
        new_node = Node(data)  # create object for the new node
        if self.head is not None:  # iterate through till end of the list
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node  # when end is reached, update next element to the new node
        else:
            self.head = new_node  # if list was empty, update head as new node

    # define method for printing linked list
    def print_list(self):
        val = self.head
        while val is not None:
            print(val.data + ' -> ', end='')
            val = val.next
        print('None')

    # method for finding length of linked list
    def count_nodes(self):
        length = 0
        num = self.head

        while num is not None:
            length += 1
            num = num.next
        print(length)


# create node class
class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


# instantiate linked list
lnk_list = LinkedList()

# create head of linked list
lnk_list.insert('Monday')

# create additional nodes
lnk_list.insert('Tuesday')
lnk_list.insert('Wednesday')


# display linked list and length
lnk_list.print_list()
lnk_list.count_nodes()
