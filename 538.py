# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root):
        
        sumOfNodes = 0
        
        def traverse(node):
            if not node:
                return
            
            nonlocal sumOfNodes

            if node.right:
                traverse(node.right)
            
            # Update
            temp = node.val
            node.val += sumOfNodes
            sumOfNodes += temp
            
            if node.left:
                traverse(node.left)

        traverse(root)
        return root