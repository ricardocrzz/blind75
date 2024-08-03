class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        # 2,3
        rest = head.next.next
        # 1 
        next = head.next
        # 0
        head.next = None
        while True:
            next.next = head
            head = next
            next = rest
            if next == None:
                return head
            rest = rest.next