class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    start = [i,j]
                    # print(grid[start[0]][start[1]])
                    break
        self.count = 0
        self.search(start,n,m)
        return self.count
    
    def search(self,start,n,m):
        if self.grid[start[0]][start[1]] == 2:
            flag = False
            for i in self.grid:
                for j in i:
                    if j==0:
                        flag = True
            if not flag:
                self.count+=1
            return
        tmp = self.grid[start[0]][start[1]]
        # print(start[0],start[1],self.grid[start[0]][start[1]])
        self.grid[start[0]][start[1]] = -1
        for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0<=start[0]+i<n and 0<=start[1]+j<m and self.grid[start[0]+i][start[1]+j]!=-1:
                self.search([start[0]+i,start[1]+j],n,m)
        self.grid[start[0]][start[1]] = tmp
        return 
        

        

grid = [[1,0,0,0],
        [0,0,0,0],
        [0,0,2,-1]]
grid =[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# grid = [[1,0],[0,2]]
# grid = [[0,1],[2,0]]
s = Solution()
ans = s.uniquePathsIII(grid)
print(ans)