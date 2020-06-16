 def swapPairs(head):
        if head is None or head.next is None:
            return head
        p = head.next 
        head.next = swapPairs(head.next.next)
        p.next = head
        return p 