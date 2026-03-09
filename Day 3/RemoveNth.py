class Solution(object):
    def removeNthFromEnd(self, head, n):
        f, s = head, head
        for _ in range(n):
            f = f.next
        if not f:
            return head.next
        while f.next:
            f,s = f.next, s.next
        s.next = s.next.next
        return head 

        