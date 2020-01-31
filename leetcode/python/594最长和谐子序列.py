class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
            if i-1 in dic:
                dic[i-1]+=1
            else:
                dic[i-1] = 1
        print(dic)
    
s = Solution()
s.findLHS([1,3,2,2,5,2,3,7])
