# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        node = []
        rank = 0
        i = 0
        while i < len(S):
            if S[i]!='-':
                word = ''
                while( i<len(S) and S[i]!='-'):
                    word+=S[i]
                    i+=1
                node.append([word,rank])
                rank = 0
                continue
            i+=1
            rank+=1
        root = TreeNode(node[0][0])
        # print(node)
        self.n = 1
        self.dfs(root,node,node[0][1]+1)
        # show(root)
        return root

    def dfs(self,root,node,layer):
        if self.n == len(node):
            # print(layer,n,'end')
            return
        if layer != node[self.n][1]:
            # print(node[self.n],layer,self.n,'not the layer')
            return 
        # print(node[n],layer,n,'normal')
        root.left = TreeNode(node[self.n][0])
        # print(layer,self.n,'left',root.left.val)
        self.n += 1
        self.dfs(root.left,node,layer+1)
        if self.n == len(node):
            # print(layer,n,'end')
            return
        if layer != node[self.n][1]:
            return 
        root.right = TreeNode(node[self.n][0])
        # print(layer,self.n,'right',root.right.val)
        self.n+=1
        self.dfs(root.right,node,layer+1)

def show(root):
    print(root.val)
    if root.left != None:
        show(root.left)
    if root.right!= None:
        show(root.right)

test = TreeNode(1)
test.left = TreeNode(2)
test.right = TreeNode(3)
show(test)
tree = "1-401--349---90--88"
s = Solution()
root = s.recoverFromPreorder(tree)
show(root)