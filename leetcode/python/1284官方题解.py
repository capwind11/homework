import collections
class Solution:
    def encode(self,mat,n,m):
        total = 0
        for i in range(n):
            for j in range(m):
                total = total*2+mat[i][j]
        return total

    def decode(self,x,n,m):
        mat = [[0]*m for _ in range(n) ]
        for i in range(n):
            for j in range(m):
                mat[n-i-1][m-j-1]=x%2
                x = x//2
        return mat
    
    def convert(self,mat,i,j,n,m):
        for (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
            i0, j0 = i + di, j + dj
            if 0 <= i0 < n and 0 <= j0 < m:
                mat[i0][j0] ^= 1
    
    def minFlips(self, mat):
        n = len(mat)
        m = len(mat[0])
        que = collections.deque()
        x = self.encode(mat,n,m)
        step = 0 
        if x == 0:
            return step
        que.append([x,step])
        visited = {x}
        while que:
            [x,step] = que.popleft()
            mat = self.decode(x,n,m)
            if x == 0:
                # print(mat)
                return step
            for i in range(n):
                for j in range(m):
                    self.convert(mat,i,j,n,m)
                    x0 = self.encode(mat,n,m)
                    if x0 in visited:
                        mat = self.decode(x,n,m)
                        continue
                    que.append([x0,step+1])
                    visited.add(x0)
                    mat = self.decode(x,n,m)
        return -1

s = Solution()
mat = [[1,0],[1,1]]
# x = s.encode(mat,2,2)
# mat = s.decode(x,2,2)
# print(x)
# print(mat)
# s.convert(mat,1,1,2,2)
# print(mat)
mat = [[1,1,1],[1,0,1],[0,0,0]]
# mat = [[0,0],[0,1]]
mat = [[1,0,0],[1,0,0]]
print(s.minFlips(mat))