class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.table = [[0]*n for _ in range(n)]
        self.count = 0
        self.size = n
        self.dfs(0)
        return self.count

    def dfs(self,row):
        tmp = []
        if row>=self.size:
            self.count+=1
            # show(self.table)
            return
        for i in range(self.size):
            tmp.append([j for j in self.table[i]])
        for i in range(self.size):
            if self.table[row][i]!=1:
                for j in range(self.size):
                    self.table[row][j]=1
                    self.table[j][i]=1
                # show(self.table)
                for j in range(row+1,self.size):
                    if (row+i-j)>=0:
                        self.table[j][row+i-j]=1
                    if (j+i-row)<self.size:
                        self.table[j][j+i-row]=1
                self.table[row][i]=2
                # show(self.table)
                self.dfs(row+1)
            self.table = []
            for j in range(self.size):
                self.table.append([e for e in tmp[j]])
            # show(self.table)
def show(m):
    for i in m:
        print(i)
    print('')
s = Solution()
print(s.totalNQueens(5))