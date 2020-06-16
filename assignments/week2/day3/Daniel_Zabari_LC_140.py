class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next
        if length <= 2:
            return head
        half = length // 2
        current = head
        for i in range(half):
            prev = current
            current = current.next
        prev.next = None
        first = head
        second = self.reverse_list(current)
        current = first
        while first is not None:
            current = first
            first = first.next
            current.next = second
            temp = second.next
            second.next = first
            second = temp
        if (length % 2) != 0:
            second.next = None
            current.next.next = second
        return head

    def reverse_list(self, head: ListNode) -> ListNode:
        current = head
        while current is not None:
            temp = current.next
            current.next = head
            head = current
            current = temp
        return head
