def invertTree(self,root):
    # exit condition
    if root is None:
        return None
    
    root.left, root.right = root.right, root.left
    
    #recursion
    self.invertTree(root.left)
    self.invertTree(root.right)
    
    return root