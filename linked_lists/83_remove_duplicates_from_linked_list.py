class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while (cur):
            if (cur.next and cur.val == cur.next.val):
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head
