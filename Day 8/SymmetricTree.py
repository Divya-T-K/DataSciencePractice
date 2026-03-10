class Solution(object):
    def isSymmetric(self, root):
        return self.same(root.left,root.right)
    def same(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if(p.val!=q.val):
            return False
        return self.same(p.left,q.right) and self.same(p.right,q.left)
        