# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def search(self,node,level):
        if not node:
            return
        if len(self.layer)<level:
            self.layer.append([node.val])
        else:
            self.layer[level-1].append(node.val)


        if node.left:
            self.search(node.left,level+1)
        if node.right:
            self.search(node.right,level+1)
        return

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.layer=[]
        level=1
        self.search(root,level)
        res=[]
        for items in self.layer:
            res.append(items[-1])
        return res
