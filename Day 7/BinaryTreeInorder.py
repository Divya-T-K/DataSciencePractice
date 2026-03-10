class Solution(object):
    def inorderTraversal(self, root):
        result = []
        self.inorder(root,result)
        return result
    def inorder(self,root,result):
        if(root == None):
            return 
        self.inorder(root.left,result)
        result.append(root.val)
        self.inorder(root.right,result)