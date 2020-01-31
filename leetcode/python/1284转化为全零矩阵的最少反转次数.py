import collections
class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        self.que = collections.deque()
        self.que.append([self.copy(mat),0])
        steps = 0
        self.n = len(mat)
        self.m = len(mat[0])
        # self.switch(1,0,mat)
        # print(mat)
        return self.bfs(steps)
    
    def bfs(self,steps):
        his = []
        while self.que:
            now,steps = self.que.popleft()
            # show(now)
            # if steps == 3:
            #     return -1
            his.append(self.copy(now))
            if self.check(now):
                # print(now)
                return steps
            tmp = self.copy(now)
            for i in range(self.n):
                for j in range(self.m):
                    self.switch(i,j,now)
                    if now in his:
                        now = self.copy(tmp)
                        continue                       
                    self.que.append([self.copy(now),steps+1])
                    now = self.copy(tmp)
        return -1
                
                
    
    def switch(self,i,j,mat):
        for num in [-1,1]:
            if j+num<self.m and j+num>=0:
                if mat[i][j+num] == 1:
                    mat[i][j+num]=0
                else:
                    mat[i][j+num]=1
        for num in [-1,1]:
            if i+num<self.n and i+num>=0:
                if mat[i+num][j] == 1:
                    mat[i+num][j]=0
                else:
                    mat[i+num][j]=1
        if mat[i][j] == 1:
            mat[i][j]=0
        else:
            mat[i][j]=1
    
    def check(self,mat):
        for i in mat:
            for j in i:
                if j == 1:
                    return False
        return True
    
    def copy(self,mat):
        tmp = [[j for j in i] for i in mat]
        return tmp

def show(mat):
    for i in mat:
        print(i)
    print('')
s = Solution()
mat = [[1,1,0],[1,0,0],[0,0,0]]
# mat = [[0,0],[1,0]]
print(s.minFlips(mat))