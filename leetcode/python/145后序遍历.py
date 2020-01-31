# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dq = collections.deque()
        ans = []
        if root:
            dq.append(root)
        while dq:
            now = dq[-1]
            if now.left==None and now.right == None:
                tmp = dq[-1]
                dq.pop()
                ans.append(tmp.val)
                continue
            if now.right:
                dq.append(now.right)
                now.right = None
            if now.left:
                dq.append(now.left)
                now.left = None
        return ans

root = TreeNode(1)
root.right = TreeNode(2)
print(root.right.val)
root.right.left = TreeNode(3)
s = Solution()
ans = s.postorderTraversal(root)
print(ans)