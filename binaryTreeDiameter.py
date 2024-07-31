# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.top = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    def func(self, root: Optional[TreeNode]) -> int:
        if root is None:
            print(node.val," is a leaf")
            return 0
        l = root.left
        r = root.right
        tl = 0
        tr = 0
        lb = True
        rb = True
        if l is not None:
            tl = self.maxDepth(l)
            print(root.val," has a left height of ",tl)
        else:
            print(root.val," has a left leaf")
            lb = False
        if r is not None:
            tr = self.maxDepth(r)
            print(root.val," has a right height of ",tr)
        else:
            print(root.val," has a right leaf")
            rb = False
        if tl+tr>self.top:
            self.top = tl+tr
        print("the value is ", root.val," and the top is ",self.top)
        print("lb is ", lb," rb is ",rb)
        if lb:
            self.func(l)
        if rb:
            self.func(r)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.top = 0
        self.func(root)
        return self.top


class Solution:
    def __init__(self):
        self.top = 0
    def depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
    
        heightLeft = self.depth(root.left)
        heightRight = self.depth(root.right)

        if heightLeft+heightRight>self.top:
            self.top = heightLeft+heightRight

        return 1 + max(heightLeft,heightRight)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.top = 0
        self.depth(root)
        return self.top
