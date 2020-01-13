class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def DutchFlagLL(head, key):
    tail = None
    curr = head
    temp = head

    # Figures out the last node in the list for help later on
    """ while curr != None:
        curr = curr.next
        if curr.next is None:
            tail = curr
            break
    # Reset curr pointer
    curr = head
    key_seen = False """

    greater = []
    less = []
    while curr.data != key:
        if curr.data > key:
            #print(head.data)
            curr = curr.next
            head = curr
        else:
            curr = curr.next

    while node:
        node_head = greater[node_index]
        print(node_head.data)
        node_head = node_head.next
    #print(node_head.data)

    #
    """ while curr != None:
        if not key_seen:
            if curr.next.data == key and curr.data > key:
                prev = curr.next
            if curr.next.data == key and curr.data < key:
                prev = curr
            if curr.data == key:
                key_seen = True
            if curr.data > key:
                head = curr.next
                curr.next = None
                tail.next = curr
                tail = curr
                curr = head
            else:
                curr = curr.next
        else:
            if curr.data < key:
                head.next = curr.next
                curr.next = head
                #prev.next = curr
                prev = curr
                curr = head.next
                print(curr.data)
            else:
                curr = curr.next
    print(prev.data) """


""" 
    while head != None:
        print(head.data)
        head = head.next """

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node2.next = node1
node3.next = node2
node4.next = node3
node5.next = node4

DutchFlagLL(node5, 3)
