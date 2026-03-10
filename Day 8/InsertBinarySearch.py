class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        root1 = root
        while True:
            if val > root1.val:
                if root1.right:
                    root1 = root1.right
                else:
                    root1.right = TreeNode(val)
                    break
            else:
                if root1.left:
                    root1 = root1.left
                else:
                    root1.left = TreeNode(val)
                    break
        return root