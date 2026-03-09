class Solution(object):
    def hasCycle(self, head):
        s = head
        f = head
        while f is not None and f.next is not None:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False