class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        elif (root.left == None and root.right == None):
            return [root.val]
        else:
            my_root_list = []
            my_root_list += [root.val]
            my_root_list += self.preorderTraversal(root.left)
            my_root_list += self.preorderTraversal(root.right)
            return my_root_list
