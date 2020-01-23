def reverseList(self, head: ListNode) -> ListNode:
    curr = head

    while curr and curr.next != None:
        prev = curr
        curr = curr.next

        prev.next = curr.next
        curr.next = head
        head = curr
        curr = prev
    return head
