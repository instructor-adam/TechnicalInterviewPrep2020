class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        if head.next is None:
            return head
        first = head
        second = head.next
        temp = second.next
        second.next = first
        first.next = temp
        head = second
        while temp is not None:
            if temp.next is not None:
                first.next = temp.next
                second = temp.next
                first = temp
                temp = second.next
                second.next = first
                first.next = temp
            else:
                break
        return head
