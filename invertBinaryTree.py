class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        #invert children of the LEFT CHILD OF ROOT
        temp = root.left.left
        root.left.left = root.left.right
        root.left.right = temp
        #invert children of the RIGHT CHILD OF ROOT
        temp = root.right.left
        root.right.left = root.right.right
        root.right.right = temp

        temp = root.left
        root.left = root.right
        root.right = temp

        return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
