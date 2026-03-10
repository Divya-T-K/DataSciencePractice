class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0 
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return 1 + max(l,r)