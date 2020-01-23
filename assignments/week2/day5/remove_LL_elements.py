def removeElements(self, head: ListNode, val: int) -> ListNode:
    curr = head
    prev = None

    while curr != None:
        if curr.val == val and curr == head:
            if curr.next is None:
                return None
            curr = curr.next
            head = curr

        elif curr.val == val:
            prev.next = curr.next
            curr = prev.next
        else:
            prev = curr
            curr = curr.next
    return head