class Solution(object):

    def postorder(self, root, result):
        if root is None:
            return
        self.postorder(root.left, result)
        self.postorder(root.right, result)
        result.append(root.val)

    def postorderTraversal(self, root):
        result = []
        self.postorder(root, result)
        return result